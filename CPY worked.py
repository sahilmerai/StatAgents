from typing import Annotated, Optional
import os
from typing import Dict, Any, Annotated
import subprocess
import os
import tempfile
import json
import pandas as pd
import numpy as np
import re
from datetime import datetime
import sys


def convert_paths_for_docker(code: str) -> str:
    """
    Convert all ./data/ paths to absolute /data/ for Docker container.
    
    WHY THIS IS CRITICAL:
    =====================
    Docker mounts:  Host ./coding/ → Container /workspace (working dir)
                    Host ./data/   → Container /data/ (volume)
    
    If agent writes: './data/Raw_data/file.csv'
    Docker resolves: /workspace/data/Raw_data/file.csv  ← WRONG (inside coding/)
    We need:         /data/Raw_data/file.csv             ← CORRECT (mounted volume)
    
    This function rewrites ALL ./data/ references to /data/ before execution.
    """
    
    # ──────────────────────────────────────────────────────────────
    # STEP 1: Convert './data/' and "./data/" → '/data/' and "/data/"
    # This is the MAIN fix — catches 95% of cases:
    #   file_path = './data/Raw_data/file.csv'
    #   pd.read_csv('./data/Raw_data/file.csv')
    #   df.to_csv('./data/Processed_data/file.csv')
    #   plt.savefig('./data/Output/Plots/chart.png')
    #   open('./data/Output/Report/report.json')
    #   os.path.exists('./data/Processed_data/file.csv')
    #   f'./data/Raw_data/{name}.csv'
    # ──────────────────────────────────────────────────────────────
    code = code.replace("'./data/", "'/data/")
    code = code.replace('"./data/', '"/data/')
    
    # ──────────────────────────────────────────────────────────────
    # STEP 2: Handle bare 'data/Raw_data/...' without ./ prefix
    #   pd.read_csv('data/Raw_data/file.csv')
    # ──────────────────────────────────────────────────────────────
    code = re.sub(
        r"(['\"])data/(Raw_data|Processed_data|Output)/",
        r"\1/data/\2/",
        code
    )
    
    # ──────────────────────────────────────────────────────────────
    # STEP 3: Remove os.makedirs lines that create /data/ dirs
    # These would create dirs inside /workspace (coding/) — WRONG
    # Host directories already exist under ./data/
    # ──────────────────────────────────────────────────────────────
    lines = code.split('\n')
    filtered_lines = []
    for line in lines:
        stripped = line.strip()
        # Skip actual code lines (not comments) that makedirs for /data/
        if not stripped.startswith('#') and 'os.makedirs' in stripped and '/data/' in stripped:
            continue
        filtered_lines.append(line)
    code = '\n'.join(filtered_lines)
    
    # ──────────────────────────────────────────────────────────────
    # STEP 4: Redirect ./output/ paths to /data/Output/Plots/
    # Some agents might use ./output/ for saving
    # ──────────────────────────────────────────────────────────────
    code = code.replace("'./output/", "'/data/Output/Plots/")
    code = code.replace('"./output/', '"/data/Output/Plots/')
    
    return code


def execute_python_code(code: Annotated[str, "Python code to execute"]) -> str:
    """
    Executes Python code in Docker container with comprehensive logging.
    
    HOST → DOCKER MAPPING:
    ┌─────────────────────────┐      ┌──────────────────────┐
    │ Host (Windows)          │      │ Docker Container     │
    │                         │      │                      │
    │ ./coding/ ──────────────┼─────→│ /workspace (workdir) │
    │   └── temp_script.py    │      │   └── temp_script.py │
    │                         │      │                      │
    │ ./data/ ────────────────┼─────→│ /data/               │
    │   ├── Raw_data/         │      │   ├── Raw_data/      │
    │   ├── Processed_data/   │      │   ├── Processed_data/│
    │   └── Output/           │      │   └── Output/        │
    │       ├── Plots/        │      │       ├── Plots/     │
    │       └── Report/       │      │       └── Report/    │
    └─────────────────────────┘      └──────────────────────┘
    
    Returns output or error message.
    """
    import time
    
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # ✅ CONVERT ALL PATHS FOR DOCKER (./data/ → /data/)
        code = convert_paths_for_docker(code)
        
        # ✅ Ensure HOST directories exist (these are OUTSIDE coding/)
        os.makedirs("./coding/logs", exist_ok=True)
        os.makedirs("./data/Raw_data", exist_ok=True)
        os.makedirs("./data/Processed_data", exist_ok=True)
        os.makedirs("./data/Output/Plots", exist_ok=True)
        os.makedirs("./data/Output/Report", exist_ok=True)
        
        # Get ABSOLUTE paths for Docker -v mounts
        coding_dir = os.path.abspath("./coding")
        data_dir = os.path.abspath("./data")
        
        # Write path-corrected code to temp file
        temp_file = os.path.join(coding_dir, "temp_script.py")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code)
        
        # Docker: mount coding/ → /workspace AND data/ → /data/
        cmd = [
            "docker", "run",
            "--rm",
            "-v", f"{coding_dir}:/workspace",
            "-v", f"{data_dir}:/data",
            "-w", "/workspace",
            "my-code-executor",
            "python", "temp_script.py"
        ]
        
        # Execute
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )
        
        execution_time = time.time() - start_time
        
        # Build response
        output = []
        if result.stdout:
            output.append(result.stdout.strip())
        if result.stderr:
            output.append(f"Warnings/Errors:\n{result.stderr.strip()}")
        
        success = result.returncode == 0
        if success:
            output.append(f"\n✅ Execution successful ({execution_time:.2f}s)")
        else:
            output.append(f"\n❌ Exit code: {result.returncode}")
        
        response_text = "\n".join(output) if output else "Code executed (no output)"
        
        # Log to file
        log_file = os.path.join("./coding/logs", "execution.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"EXECUTION LOG - {timestamp}\n")
            f.write(f"{'='*80}\n")
            f.write(f"Duration: {execution_time:.2f}s | Success: {success} | Exit Code: {result.returncode}\n")
            f.write(f"\nCODE (path-corrected for Docker):\n{'-'*80}\n{code}\n")
            f.write(f"\nOUTPUT:\n{'-'*80}\n{result.stdout}\n")
            if result.stderr:
                f.write(f"\nERRORS/WARNINGS:\n{'-'*80}\n{result.stderr}\n")
            f.write(f"{'='*80}\n\n")
        
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        return response_text
        
    except subprocess.TimeoutExpired:
        return "⏱️ Execution timeout (>120s)"
    except Exception as e:
        error_msg = f"🔥 Error: {type(e).__name__}: {str(e)}"
        
        log_file = os.path.join("./coding/logs", "execution.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"EXECUTION ERROR - {timestamp}\n")
            f.write(f"{'='*80}\n")
            f.write(f"{error_msg}\n")
            f.write(f"CODE:\n{code}\n")
            f.write(f"{'='*80}\n\n")
        
        return error_msg
    

def execute_python_code_T(code: Annotated[str, "Python code to execute"]) -> str:
    """
    Same as execute_python_code but with extended timeout (300s).
    Used for longer tasks: time series, DOE, heavy computations.
    """
    import time
    
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # ✅ CONVERT ALL PATHS FOR DOCKER (./data/ → /data/)
        code = convert_paths_for_docker(code)
        
        # ✅ Ensure HOST directories exist
        os.makedirs("./coding/logs", exist_ok=True)
        os.makedirs("./data/Raw_data", exist_ok=True)
        os.makedirs("./data/Processed_data", exist_ok=True)
        os.makedirs("./data/Output/Plots", exist_ok=True)
        os.makedirs("./data/Output/Report", exist_ok=True)
        
        # Get ABSOLUTE paths for Docker -v mounts
        coding_dir = os.path.abspath("./coding")
        data_dir = os.path.abspath("./data")
        
        # Write path-corrected code to temp file
        temp_file = os.path.join(coding_dir, "temp_script.py")
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(code)
        
        # Docker: mount coding/ → /workspace AND data/ → /data/
        cmd = [
            "docker", "run",
            "--rm",
            "-v", f"{coding_dir}:/workspace",
            "-v", f"{data_dir}:/data",
            "-w", "/workspace",
            "my-code-executor",
            "python", "temp_script.py"
        ]
        
        # Execute with extended timeout
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        execution_time = time.time() - start_time
        
        # Build response
        output = []
        if result.stdout:
            output.append(result.stdout.strip())
        if result.stderr:
            output.append(f"Warnings/Errors:\n{result.stderr.strip()}")
        
        success = result.returncode == 0
        if success:
            output.append(f"\n✅ Execution successful ({execution_time:.2f}s)")
        else:
            output.append(f"\n❌ Exit code: {result.returncode}")
        
        response_text = "\n".join(output) if output else "Code executed (no output)"
        
        # Log to file
        log_file = os.path.join("./coding/logs", "execution.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"EXECUTION LOG - {timestamp}\n")
            f.write(f"{'='*80}\n")
            f.write(f"Duration: {execution_time:.2f}s | Success: {success} | Exit Code: {result.returncode}\n")
            f.write(f"\nCODE (path-corrected for Docker):\n{'-'*80}\n{code}\n")
            f.write(f"\nOUTPUT:\n{'-'*80}\n{result.stdout}\n")
            if result.stderr:
                f.write(f"\nERRORS/WARNINGS:\n{'-'*80}\n{result.stderr}\n")
            f.write(f"{'='*80}\n\n")
        
        # Clean up temp file
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        return response_text
        
    except subprocess.TimeoutExpired:
        return "⏱️ Execution timeout (>300s)"
    except Exception as e:
        error_msg = f"🔥 Error: {type(e).__name__}: {str(e)}"
        
        log_file = os.path.join("./coding/logs", "execution.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n{'='*80}\n")
            f.write(f"EXECUTION ERROR - {timestamp}\n")
            f.write(f"{'='*80}\n")
            f.write(f"{error_msg}\n")
            f.write(f"CODE:\n{code}\n")
            f.write(f"{'='*80}\n\n")
        
        return error_msg

    
if __name__ == "__main__":
    print("=" * 60)
    print("CPY.py PATH CONVERSION TEST")
    print("=" * 60)
    
    test_code = """import pandas as pd
import os

# Variable assignment
file_path = './data/Raw_data/metrics_results_final.csv'
df = pd.read_csv(file_path)

# Direct function calls
df = pd.read_csv('./data/Raw_data/Tractor_Sales.csv')
df = pd.read_csv("./data/Processed_data/file_processed.csv")
df.to_csv('./data/Processed_data/output_processed.csv', index=False)
plt.savefig('./data/Output/Plots/chart.png')

# f-string
name = "test"
path = f'./data/Raw_data/{name}.csv'

# open()
with open('./data/Output/Report/analysis.json', 'w') as f:
    json.dump(data, f)

# os.makedirs that should be REMOVED
os.makedirs('./data/Processed_data', exist_ok=True)
os.makedirs("./data/Output/Plots", exist_ok=True)

# ./output/ redirect
plt.savefig('./output/my_plot.png')

# bare data/ path
df = pd.read_csv('data/Raw_data/file.csv')

# os.path checks
if os.path.exists('./data/Processed_data/file.csv'):
    pass
"""
    
    converted = convert_paths_for_docker(test_code)
    
    print("\n--- CONVERTED CODE ---")
    print(converted)
    print("--- END ---\n")
    
    # Validate
    errors = []
    for i, line in enumerate(converted.split('\n'), 1):
        stripped = line.strip()
        if stripped.startswith('#'):
            continue
        
        # Check for unconverted ./data/ paths
        if "'./data/" in stripped or '"./data/' in stripped:
            errors.append(f"  Line {i}: UNCONVERTED ./data/ → {stripped}")
        
        # Check for os.makedirs /data/ lines
        if 'os.makedirs' in stripped and '/data/' in stripped:
            errors.append(f"  Line {i}: MAKEDIRS not removed → {stripped}")
        
        # Check for ./output/ paths
        if "'./output/" in stripped or '"./output/' in stripped:
            errors.append(f"  Line {i}: UNCONVERTED ./output/ → {stripped}")
    
    # Check that correct paths exist
    expected = [
        "'/data/Raw_data/metrics_results_final.csv'",
        "'/data/Raw_data/Tractor_Sales.csv'",
        '"/data/Processed_data/file_processed.csv"',
        "'/data/Processed_data/output_processed.csv'",
        "'/data/Output/Plots/chart.png'",
        "'/data/Output/Report/analysis.json'",
        "'/data/Raw_data/file.csv'",
    ]
    
    for exp in expected:
        if exp not in converted:
            errors.append(f"  MISSING expected path: {exp}")
    
    if errors:
        print("❌ ERRORS FOUND:")
        for e in errors:
            print(e)
    else:
        print("✅ ALL TESTS PASSED!")
        print("  ✓ ./data/ → /data/ conversion")
        print("  ✓ bare data/ → /data/ conversion")
        print("  ✓ os.makedirs lines removed")
        print("  ✓ ./output/ redirected")
        print("  ✓ All expected paths present")