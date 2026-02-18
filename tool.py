# tool.py
from typing import Annotated, Optional
import os
from pylatex import Document, Section, Subsection, Command, Figure, Table, Math, NoEscape
from pylatex.utils import italic, bold
from typing import Dict, Any, Annotated
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from autogen_core.code_executor import CodeBlock
# from Rag import load_faiss_index
import subprocess
import os
import tempfile
import json
import pandas as pd
import numpy as np
import re
from datetime import datetime
from scipy import stats
import sys
load_dotenv()




def analyze_csv_data(filepath: Annotated[str, "Path to CSV file - automatically checks both ./data/Raw_data/ and ./data/Processed_data/"], 
                     use_processed: Annotated[bool, "Set True to prioritize processed data folder"] = False) -> str:
    """
    Performs comprehensive EDA on uploaded CSV file.
    Returns JSON with all statistics and saves to ./data/Output/Report/filename_analysis.json
    Automatically checks both raw and processed data folders.
    """
    try:
        # Setup paths - FIXED STRUCTURE
        raw_data_dir = "./data/Raw_data"
        processed_dir = "./data/Processed_data"
        output_dir = "./data/Output/Report"
        
        # Ensure folders exist
        os.makedirs(raw_data_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Clean filepath - extract just the filename
        # Handle various input formats users might provide
        original_filepath = filepath
        
        # Remove common path prefixes to get just filename
        prefixes_to_remove = [
            "./data/Raw_data/",
            "./data/Processed_data/",
            "data/Raw_data/",
            "data/Processed_data/",
            "./data/",
            "data/",
        ]
        
        filename = filepath
        for prefix in prefixes_to_remove:
            if filename.startswith(prefix):
                filename = filename[len(prefix):]
                break
        
        # Now filename should be just "Tractor_Sales.csv" or similar
        
        # Determine which file to analyze
        full_path = None
        is_processed = False
        
        if use_processed:
            # Check processed folder first
            # Handle both "file.csv" and "file_processed.csv" naming
            processed_filename = filename
            if not processed_filename.endswith('_processed.csv'):
                processed_filename = filename.replace('.csv', '_processed.csv')
            
            processed_path = os.path.join(processed_dir, processed_filename)
            
            if os.path.exists(processed_path):
                full_path = processed_path
                is_processed = True
            else:
                # Also try original filename in processed folder
                alt_processed_path = os.path.join(processed_dir, filename)
                if os.path.exists(alt_processed_path):
                    full_path = alt_processed_path
                    is_processed = True
        
        # If not found in processed (or use_processed=False), check raw folder
        if full_path is None:
            raw_path = os.path.join(raw_data_dir, filename)
            if os.path.exists(raw_path):
                full_path = raw_path
                is_processed = False
        
        # If still not found, try processed folder as fallback
        if full_path is None and not use_processed:
            processed_filename = filename.replace('.csv', '_processed.csv')
            processed_path = os.path.join(processed_dir, processed_filename)
            if os.path.exists(processed_path):
                full_path = processed_path
                is_processed = True
            else:
                # Try original filename in processed
                alt_path = os.path.join(processed_dir, filename)
                if os.path.exists(alt_path):
                    full_path = alt_path
                    is_processed = True
        
        # Check if file exists
        if full_path is None or not os.path.exists(full_path):
            available_raw = os.listdir(raw_data_dir) if os.path.exists(raw_data_dir) else []
            available_processed = os.listdir(processed_dir) if os.path.exists(processed_dir) else []
            
            return f"""❌ File not found: {original_filepath}

**Extracted filename:** {filename}

**Searched locations:**
- Raw data: {os.path.join(raw_data_dir, filename)}
- Processed: {os.path.join(processed_dir, filename.replace('.csv', '_processed.csv'))}

**Available files:**
- Raw data folder ({raw_data_dir}): {available_raw}
- Processed data folder ({processed_dir}): {available_processed}

**Tip:** Use one of these formats:
- analyze_csv_data('./data/Raw_data/Tractor_Sales.csv')
- analyze_csv_data('Tractor_Sales.csv')
- analyze_csv_data('./data/Processed_data/Tractor_Sales_processed.csv', use_processed=True)"""
        
        # Read CSV
        df = pd.read_csv(full_path)
        
        # Initialize analysis dictionary
        analysis = {
            "dataset_info": {
                "filename": os.path.basename(full_path),
                "is_processed_data": is_processed,
                "file_location": full_path,
                "rows": len(df),
                "columns": len(df.columns),
                "column_names": list(df.columns),
                "total_cells": df.size,
                "memory_usage_mb": round(df.memory_usage(deep=True).sum() / 1024**2, 2),
                "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "data_type_identification": {},
            "column_dtypes": df.dtypes.astype(str).to_dict(),
            "missing_summary": {
                "total_missing": int(df.isnull().sum().sum()),
                "total_missing_pct": round(df.isnull().sum().sum() / df.size * 100, 2),
                "columns_with_missing": {}
            },
            "duplicates": {
                "duplicate_rows": int(df.duplicated().sum()),
                "duplicate_pct": round(df.duplicated().sum() / len(df) * 100, 2)
            },
            "numerical_analysis": {},
            "categorical_analysis": {},
            "correlations": {}
        }
        
        # Missing values per column
        for col in df.columns:
            missing_count = df[col].isnull().sum()
            if missing_count > 0:
                analysis["missing_summary"]["columns_with_missing"][col] = {
                    "count": int(missing_count),
                    "percentage": round(missing_count / len(df) * 100, 2)
                }
        
        # DATA TYPE IDENTIFICATION
        data_type_hints = identify_data_structure(df)
        analysis["data_type_identification"] = data_type_hints
        
        # Numerical columns analysis
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            data = df[col].dropna()
            
            if len(data) == 0:
                continue
            
            # Outlier detection using IQR
            Q1 = data.quantile(0.25)
            Q3 = data.quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = data[(data < lower_bound) | (data > upper_bound)]
            
            # Distribution shape
            skew_val = data.skew()
            kurt_val = data.kurtosis()
            
            if skew_val > 0.5:
                skew_type = "right-skewed (positive)"
            elif skew_val < -0.5:
                skew_type = "left-skewed (negative)"
            else:
                skew_type = "approximately symmetric"
            
            if kurt_val > 3:
                kurt_type = "leptokurtic (heavy-tailed)"
            elif kurt_val < -3:
                kurt_type = "platykurtic (light-tailed)"
            else:
                kurt_type = "mesokurtic (normal-like)"
            
            # Mode handling (multimodal detection)
            mode_series = data.mode()
            mode_val = float(mode_series[0]) if len(mode_series) > 0 else None
                        
            analysis["numerical_analysis"][col] = {
                "count": int(data.count()),
                "missing": int(df[col].isnull().sum()),
                "missing_pct": round(df[col].isnull().sum() / len(df) * 100, 2),
                "mean": round(float(data.mean()), 4),
                "median": round(float(data.median()), 4),
                "mode": mode_val,
                "std": round(float(data.std()), 4),
                "variance": round(float(data.var()), 4),
                "min": round(float(data.min()), 4),
                "max": round(float(data.max()), 4),
                "range": round(float(data.max() - data.min()), 4),
                "q1": round(float(Q1), 4),
                "q3": round(float(Q3), 4),
                "iqr": round(float(IQR), 4),
                "skewness": round(float(skew_val), 4),
                "skewness_type": skew_type,
                "kurtosis": round(float(kurt_val), 4),
                "kurtosis_type": kurt_type,
                "outliers": {
                    "count": len(outliers),
                    "percentage": round(len(outliers) / len(data) * 100, 2) if len(data) > 0 else 0,
                    "indices": outliers.index.tolist()[:50],  # Limit to first 50
                    "values": [round(float(v), 4) for v in outliers.values[:50]]
                }
            }
        
        # Categorical columns analysis
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns
        for col in categorical_cols:
            data = df[col].dropna()
            
            if len(data) == 0:
                continue
                
            value_counts = data.value_counts()
            
            analysis["categorical_analysis"][col] = {
                "count": int(data.count()),
                "missing": int(df[col].isnull().sum()),
                "missing_pct": round(df[col].isnull().sum() / len(df) * 100, 2),
                "unique_values": int(data.nunique()),
                "mode": data.mode().tolist(),
                "top_10_frequencies": value_counts.head(10).to_dict(),
                "top_value": str(value_counts.index[0]),
                "top_value_count": int(value_counts.iloc[0]),
                "top_value_pct": round(value_counts.iloc[0] / len(data) * 100, 2)
            }
        
        # Correlation analysis (numerical only)
        if len(numeric_cols) > 1:
            corr_matrix = df[numeric_cols].corr()
            
            # Find high, medium, low correlations
            high_corr = []
            medium_corr = []
            low_corr = []
            negative_corr = []
            
            for i in range(len(corr_matrix.columns)):
                for j in range(i+1, len(corr_matrix.columns)):
                    col1 = corr_matrix.columns[i]
                    col2 = corr_matrix.columns[j]
                    corr_val = corr_matrix.iloc[i, j]
                    
                    if pd.isna(corr_val):
                        continue
                    
                    pair = {
                        "var1": col1,
                        "var2": col2,
                        "correlation": round(float(corr_val), 4)
                    }
                    
                    if corr_val < 0:
                        negative_corr.append(pair)
                    elif abs(corr_val) > 0.7:
                        high_corr.append(pair)
                    elif abs(corr_val) > 0.4:
                        medium_corr.append(pair)
                    else:
                        low_corr.append(pair)
            
            analysis["correlations"] = {
                "correlation_matrix": corr_matrix.round(4).to_dict(),
                "high_correlation": sorted(high_corr, key=lambda x: abs(x["correlation"]), reverse=True),
                "medium_correlation": sorted(medium_corr, key=lambda x: abs(x["correlation"]), reverse=True),
                "low_correlation": low_corr[:10],  # Limit low correlations
                "negative_correlation": sorted(negative_corr, key=lambda x: x["correlation"])
            }
        
        # Save JSON to output folder
        json_filename = os.path.basename(full_path).replace('.csv', '_analysis.json')
        json_path = os.path.join(output_dir, json_filename)
            
        with open(json_path, 'w') as f:
            json.dump(analysis, f, indent=2)
        
        # Return formatted summary + JSON
        data_quality_issues = []
        if analysis['missing_summary']['total_missing'] > 0:
            data_quality_issues.append(f"⚠️ Missing values: {analysis['missing_summary']['total_missing']:,} cells ({analysis['missing_summary']['total_missing_pct']}%)")
        if analysis['duplicates']['duplicate_rows'] > 0:
            data_quality_issues.append(f"⚠️ Duplicate rows: {analysis['duplicates']['duplicate_rows']} ({analysis['duplicates']['duplicate_pct']}%)")
        
        # Count outliers
        total_outliers = sum(col_data['outliers']['count'] for col_data in analysis['numerical_analysis'].values())
        if total_outliers > 0:
            data_quality_issues.append(f"⚠️ Outliers detected: {total_outliers} across numerical columns")
        
        # Check for skewed distributions
        highly_skewed = [col for col, data in analysis['numerical_analysis'].items() if abs(data['skewness']) > 1]
        if highly_skewed:
            data_quality_issues.append(f"⚠️ Highly skewed columns: {', '.join(highly_skewed)}")
        
        quality_status = "\n".join(data_quality_issues) if data_quality_issues else "✅ No major data quality issues detected"
        
        summary = f"""
✅ **EDA Analysis Complete**

**Dataset:** {analysis['dataset_info']['filename']}
**Data Type:** {data_type_hints['likely_type']}
**Location:** {'Processed Data' if is_processed else 'Raw Data'}

**Dimensions:**
- Rows: {analysis['dataset_info']['rows']:,}
- Columns: {analysis['dataset_info']['columns']}
- Total cells: {analysis['dataset_info']['total_cells']:,}
- Memory: {analysis['dataset_info']['memory_usage_mb']} MB

**Data Quality:**
{quality_status}

**Column Types:**
- Numerical columns: {len(numeric_cols)}
- Categorical columns: {len(categorical_cols)}

**Correlations:**
- High correlations (>0.7): {len(analysis['correlations'].get('high_correlation', []))}
- Medium correlations (0.4-0.7): {len(analysis['correlations'].get('medium_correlation', []))}

**Analysis saved to:** `{json_path}`

**Full JSON Analysis:**
```json
{json.dumps(analysis, indent=2)}
```
"""
        return summary
        
    except FileNotFoundError:
        return f"❌ File not found: {filepath}\nMake sure CSV is uploaded to ./data/Raw_data/ folder"
    except Exception as e:
        import traceback
        return f"❌ Error analyzing CSV: {type(e).__name__}: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"


def identify_data_structure(df: pd.DataFrame) -> dict:
    """
    Identify if data is cross-sectional, panel, time series, or multivariate
    Returns detailed analysis of data structure
    """
    hints = {
        "likely_type": "Unknown",
        "confidence": "Low",
        "reasons": [],
        "detected_columns": {
            "id_columns": [],
            "time_columns": [],
            "numeric_columns": [],
            "categorical_columns": []
        },
        "recommendations": []
    }
    
    # Detect ID columns (entity identifiers)
    id_patterns = ['id', 'code', 'customer', 'product', 'store', 'entity', 'firm', 'company', 'person']
    id_cols = [col for col in df.columns if any(pattern in col.lower() for pattern in id_patterns)]
    hints["detected_columns"]["id_columns"] = id_cols
    
    # Detect time/date columns
    time_patterns = ['date', 'time', 'year', 'month', 'day', 'quarter', 'period', 'week']
    time_cols = [col for col in df.columns if any(pattern in col.lower() for pattern in time_patterns)]
    
    # Also check for datetime dtypes
    datetime_cols = df.select_dtypes(include=['datetime64']).columns.tolist()
    time_cols = list(set(time_cols + datetime_cols))
    hints["detected_columns"]["time_columns"] = time_cols
    
    # Count numeric and categorical
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    hints["detected_columns"]["numeric_columns"] = numeric_cols
    hints["detected_columns"]["categorical_columns"] = categorical_cols
    
    # DECISION LOGIC
    
    # Panel Data: Has both ID and Time columns
    if id_cols and time_cols:
        hints["likely_type"] = "Panel Data (Longitudinal)"
        hints["confidence"] = "High"
        hints["reasons"].append(f"✓ Entity ID column(s) detected: {id_cols}")
        hints["reasons"].append(f"✓ Time dimension column(s) detected: {time_cols}")
        
        # Check if balanced panel
        if id_cols and time_cols:
            id_col = id_cols[0]
            time_col = time_cols[0]
            panel_structure = df.groupby(id_col)[time_col].count()
            if panel_structure.nunique() == 1:
                hints["reasons"].append(f"✓ Balanced panel: Each entity has {panel_structure.iloc[0]} time periods")
            else:
                hints["reasons"].append(f"⚠ Unbalanced panel: Entities have varying time periods ({panel_structure.min()}-{panel_structure.max()})")
        
        hints["recommendations"].append("Use panel data models: Fixed Effects, Random Effects, or Pooled OLS")
        hints["recommendations"].append("Check for entity-specific and time-specific effects")
        
    # Time Series: Has Time but NO ID columns
    elif time_cols and not id_cols:
        hints["likely_type"] = "Time Series"
        hints["confidence"] = "High"
        hints["reasons"].append(f"✓ Time dimension detected: {time_cols}")
        hints["reasons"].append("✓ No entity ID column (single time series)")
        
        # Check for temporal patterns
        if len(df) > 30:
            hints["reasons"].append(f"✓ Sufficient observations for time series: {len(df)} periods")
        else:
            hints["reasons"].append(f"⚠ Limited observations: {len(df)} periods (may limit analysis)")
        
        hints["recommendations"].append("Check for: trend, seasonality, autocorrelation")
        hints["recommendations"].append("Consider: ARIMA, exponential smoothing, or structural models")
        hints["recommendations"].append("Test for stationarity (ADF test, KPSS test)")
        
    # Cross-Sectional: Has ID but NO Time columns
    elif id_cols and not time_cols:
        hints["likely_type"] = "Cross-Sectional"
        hints["confidence"] = "High"
        hints["reasons"].append(f"✓ Entity ID column(s) detected: {id_cols}")
        hints["reasons"].append("✓ No time dimension (single period snapshot)")
        hints["reasons"].append(f"✓ {len(df)} unique observations")
        
        hints["recommendations"].append("Use cross-sectional models: OLS regression, logit/probit")
        hints["recommendations"].append("Check for heteroscedasticity and outliers")
        
    # Multivariate (no clear ID or time)
    else:
        if len(numeric_cols) >= 3:
            hints["likely_type"] = "Multivariate Cross-Sectional"
            hints["confidence"] = "Medium"
            hints["reasons"].append(f"✓ Multiple numeric variables: {len(numeric_cols)} columns")
            hints["reasons"].append("⚠ No clear ID or time columns detected")
            hints["reasons"].append("Could be: anonymized data, survey data, or experimental data")
            
            hints["recommendations"].append("Treat as cross-sectional data")
            hints["recommendations"].append("Consider creating unique ID if needed")
        else:
            hints["likely_type"] = "Unclear Structure"
            hints["confidence"] = "Low"
            hints["reasons"].append("⚠ Unable to determine data structure")
            hints["reasons"].append(f"Columns: {list(df.columns)}")
            
            hints["recommendations"].append("Review column names and data structure")
            hints["recommendations"].append("Consider adding ID or time identifiers if applicable")
    
    # Additional checks
    if len(numeric_cols) >= 5:
        hints["reasons"].append(f"✓ Rich dataset: {len(numeric_cols)} numeric variables for analysis")
    
    return hints
    


def retrieve_graphrag_local_Doe(
    query: Annotated[str, "Specific DOE query - formulas, tests, definitions"]
) -> str:
    """Query GraphRAG LOCAL for DOE concepts."""
    try:
        cmd = [
            "graphrag",  # Changed from sys.executable, "-m", "graphrag.query"
            "query",
            "--root", r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Grag",
            "--method", "local",
            "--query", query  # Added --query flag
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode != 0:
            return f"❌ GraphRAG Error:\n{result.stderr}"
        
        # Clean output (remove deprecation warnings and logging)
        output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
        
        skip_patterns = [
            'INFO:', 'WARN:', 'ERROR:', 'DEBUG:',
            'Model config based on fnllm is deprecated',
            'creating llm', 'creating embedding',
            'Vector Store Args', 'SUCCESS:', 'No existing dataset',
            '(AI) PS F:', 'tiktoken', 'openai', 'azure'
        ]
        
        lines = output.split('\n')
        clean_lines = []
        
        for line in lines:
            if any(p in line for p in skip_patterns):
                continue
            if not clean_lines and not line.strip():
                continue
            clean_lines.append(line)
        
        result_text = '\n'.join(clean_lines).strip()
        result_text = re.sub(r'\n{3,}', '\n\n', result_text)
        
        if not result_text or len(result_text) < 10:
            return "⚠️ No content returned."
        
        return f"📚 **GraphRAG LOCAL Results**\n\n{result_text}"
        
    except FileNotFoundError:
        return "❌ 'graphrag' command not found. Check if graphrag is in PATH."
    except subprocess.TimeoutExpired:
        return "⏱️ Query timed out."
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {str(e)}"


def retrieve_graphrag_global_Doe(
    query: Annotated[str, "Broad DOE query - overviews, comparisons"]
) -> str:
    """Query GraphRAG GLOBAL for DOE overviews."""
    try:
        cmd = [
            "graphrag",  # Changed
            "query",
            "--root", r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Grag",
            "--method", "global",
            "--query", query  # Added --query flag
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode != 0:
            return f"❌ GraphRAG Error:\n{result.stderr}"
        
        # Clean output
        output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
        
        skip_patterns = [
            'INFO:', 'WARN:', 'ERROR:', 'DEBUG:',
            'Model config based on fnllm is deprecated',
            'creating llm', 'creating embedding',
            'Vector Store Args', 'SUCCESS:', 'No existing dataset',
            '(AI) PS F:', 'tiktoken', 'openai', 'azure'
        ]
        
        lines = output.split('\n')
        clean_lines = []
        
        for line in lines:
            if any(p in line for p in skip_patterns):
                continue
            if not clean_lines and not line.strip():
                continue
            clean_lines.append(line)
        
        result_text = '\n'.join(clean_lines).strip()
        result_text = re.sub(r'\n{3,}', '\n\n', result_text)
        
        if not result_text or len(result_text) < 10:
            return "⚠️ No content returned."
        
        return f"🌐 **GraphRAG GLOBAL Results**\n\n{result_text}"
        
    except FileNotFoundError:
        return "❌ 'graphrag' command not found. Check if graphrag is in PATH."
    except subprocess.TimeoutExpired:
        return "⏱️ Query timed out."
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {str(e)}"
    

def retrieve_doe_rag(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\DOE Brain\Normal Rag"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=4)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 **DOE Textbook Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"


def retrieve_graphrag_local_Eco(
    query: Annotated[str, "Specific DOE query - formulas, tests, definitions"]
) -> str:
    """Query GraphRAG LOCAL for DOE concepts."""
    try:
        cmd = [
            "graphrag",  # Changed from sys.executable, "-m", "graphrag.query"
            "query",
            "--root", r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain",
            "--method", "local",
            "--query", query  # Added --query flag
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode != 0:
            return f"❌ GraphRAG Error:\n{result.stderr}"
        
        # Clean output (remove deprecation warnings and logging)
        output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
        
        skip_patterns = [
            'INFO:', 'WARN:', 'ERROR:', 'DEBUG:',
            'Model config based on fnllm is deprecated',
            'creating llm', 'creating embedding',
            'Vector Store Args', 'SUCCESS:', 'No existing dataset',
            '(AI) PS F:', 'tiktoken', 'openai', 'azure'
        ]
        
        lines = output.split('\n')
        clean_lines = []
        
        for line in lines:
            if any(p in line for p in skip_patterns):
                continue
            if not clean_lines and not line.strip():
                continue
            clean_lines.append(line)
        
        result_text = '\n'.join(clean_lines).strip()
        result_text = re.sub(r'\n{3,}', '\n\n', result_text)
        
        if not result_text or len(result_text) < 10:
            return "⚠️ No content returned."
        
        return f"📚 **GraphRAG LOCAL Results**\n\n{result_text}"
        
    except FileNotFoundError:
        return "❌ 'graphrag' command not found. Check if graphrag is in PATH."
    except subprocess.TimeoutExpired:
        return "⏱️ Query timed out."
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {str(e)}"


def retrieve_graphrag_global_Eco(
    query: Annotated[str, "Broad DOE query - overviews, comparisons"]
) -> str:
    """Query GraphRAG GLOBAL for DOE overviews."""
    try:
        cmd = [
            "graphrag",  # Changed
            "query",
            "--root", r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain",
            "--method", "global",
            "--query", query  # Added --query flag
        ]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=300,
            encoding='utf-8',
            errors='replace'
        )
        
        if result.returncode != 0:
            return f"❌ GraphRAG Error:\n{result.stderr}"
        
        # Clean output
        output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
        
        skip_patterns = [
            'INFO:', 'WARN:', 'ERROR:', 'DEBUG:',
            'Model config based on fnllm is deprecated',
            'creating llm', 'creating embedding',
            'Vector Store Args', 'SUCCESS:', 'No existing dataset',
            '(AI) PS F:', 'tiktoken', 'openai', 'azure'
        ]
        
        lines = output.split('\n')
        clean_lines = []
        
        for line in lines:
            if any(p in line for p in skip_patterns):
                continue
            if not clean_lines and not line.strip():
                continue
            clean_lines.append(line)
        
        result_text = '\n'.join(clean_lines).strip()
        result_text = re.sub(r'\n{3,}', '\n\n', result_text)
        
        if not result_text or len(result_text) < 10:
            return "⚠️ No content returned."
        
        return f"🌐 **GraphRAG GLOBAL Results**\n\n{result_text}"
        
    except FileNotFoundError:
        return "❌ 'graphrag' command not found. Check if graphrag is in PATH."
    except subprocess.TimeoutExpired:
        return "⏱️ Query timed out."
    except Exception as e:
        return f"❌ Error: {type(e).__name__}: {str(e)}"
    

def retrieve_Eco_rag(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\ECO Brain\Normal Rag"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=4)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 **Econometric Textbook Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"

def retrieve_statistics_books(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\Statistical brain\Normal Rag"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=4)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 **Statistical_test Textbook Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"
    

def retrieve_business_story(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\HOD Brain\business_storytelling_templates"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=3)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 ** Business storytelling templates Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"
    

def retrieve_statistical_test(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\HOD Brain\statistical_test_decision_tree"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=3)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 **Statistical test decision tree Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"
    

def retrieve_workflow(
    query: Annotated[str, "Question about Design of Experiments from DOE textbook"]
) -> str:
    """Query DOE textbook using FAISS RAG for relevant context."""
    try:
        FAISS_INDEX_PATH = r"F:\Project work\Cafe Restaurant Analysis\Agents\HOD Brain\workflow_knowledge"
        
        embeddings = AzureOpenAIEmbeddings(
            azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
        
        db = FAISS.load_local(
            FAISS_INDEX_PATH, 
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = db.similarity_search(query, k=2)
        
        if not docs:
            return "⚠️ No relevant information found."
        
        results = ["📚 **Workflow Context (FAISS RAG)**\n"]
        
        for i, doc in enumerate(docs, 1):
            content = doc.page_content.strip()
            results.append(f"**Chunk {i}:**\n{content}\n")
            results.append("-" * 80 + "\n")
        
        return "\n".join(results)
        
    except Exception as e:
        return f"❌ RAG Error: {str(e)}"

# ---------------------------
# Manual test
# ---------------------------
if __name__ == "__main__":
    pass
