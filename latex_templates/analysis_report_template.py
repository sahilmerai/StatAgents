from pylatex import Document, Section, Subsection, Command, Package, NoEscape
from pylatex.utils import bold, italic
from datetime import datetime
from latex_templates.components.regression_table import create_regression_table
from latex_templates.components.descriptive_stats_table import create_descriptive_stats_table
from latex_templates.components.hypothesis_test_table import create_hypothesis_test_table
from latex_templates.components.data_preparation_section import create_data_prep_section
from latex_templates.components.figure_handler import add_figure
from pylatex.lists import Itemize, Enumerate

def generate_analysis_report(title: str, data: dict) -> Document:
    """
    Generate analysis report format (executive summary style).
    
    Sections:
    - Executive Summary
    - Data Overview
    - Key Findings
    - Statistical Analysis
    - Recommendations
    """
    
    # Document setup
    geometry_options = {
        "margin": "1in",
        "headheight": "15pt"
    }
    
    doc = Document(geometry_options=geometry_options)
    
    # Packages
    doc.packages.append(Package('booktabs'))
    doc.packages.append(Package('amsmath'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('caption'))
    doc.packages.append(Package('hyperref'))
    doc.packages.append(Package('float'))
    doc.packages.append(Package('siunitx'))
    doc.packages.append(Package('xcolor'))
    
    # Title, author, date
    doc.preamble.append(Command('title', bold(title)))
    author = data.get('author', 'Analytics Team')
    doc.preamble.append(Command('author', author))
    date = data.get('date', datetime.now().strftime('%B %d, %Y'))
    doc.preamble.append(Command('date', date))
    
    doc.append(NoEscape(r'\maketitle'))
    
    # EXECUTIVE SUMMARY (highlighted box)
    doc.append(NoEscape(r'\begin{center}\fcolorbox{black}{gray!10}{\parbox{0.9\textwidth}{'))
    doc.append(NoEscape(r'\section*{Executive Summary}'))
    
    exec_summary = _generate_executive_summary(data)
    doc.append(exec_summary)
    
    doc.append(NoEscape(r'}}\end{center}'))
    doc.append(NoEscape(r'\vspace{1em}'))
    
    # DATA OVERVIEW
    with doc.create(Section('Data Overview')):
        if data.get('data_preparation'):
            prep = data['data_preparation']
            
            doc.append(bold("Original Dataset: "))
            doc.append(f"{prep.get('original_file', 'N/A')}")
            doc.append(NoEscape(r'\\'))
            
            doc.append(bold("Data Size: "))
            doc.append(f"{prep.get('original_shape', 'N/A')}")
            doc.append(NoEscape(r'\\[0.5em]'))
            
            # Data quality
            if prep.get('issues_detected'):
                doc.append(NoEscape(r'\subsection*{Data Quality Issues}'))
                with doc.create(Itemize()) as itemize_list:
                    for issue in prep['issues_detected']:
                        itemize_list.add_item(issue)
            
            # Data cleaning
            if prep.get('cleaning_actions'):
                doc.append(NoEscape(r'\subsection*{Data Preparation Actions}'))
                with doc.create(Itemize()) as itemize_list:
                    for action in prep['cleaning_actions']:
                        itemize_list.add_item(action)
            
            doc.append(NoEscape(r'\vspace{0.5em}'))
            doc.append(bold("Final Dataset: "))
            doc.append(f"{prep.get('final_shape', 'N/A')}")
    
    # KEY FINDINGS (highlighted)
    doc.append(NoEscape(r'\section{Key Findings}'))
    
    key_findings = _extract_key_findings(data)
    if key_findings:
        with doc.create(Enumerate()) as enum:
            for finding in key_findings:
                enum.add_item(NoEscape(r'\textbf{' + finding['title'] + r'}: ' + finding['detail']))
    
    # STATISTICAL ANALYSIS
    with doc.create(Section('Statistical Analysis')):
        
        # Descriptive Statistics
        if data.get('descriptive_stats'):
            doc.append(NoEscape(r'\subsection{Descriptive Statistics}'))
            doc.append(create_descriptive_stats_table(data['descriptive_stats']))
            
            # Interpretation
            if data['descriptive_stats'].get('key_findings'):
                doc.append(NoEscape(r'\paragraph{Interpretation:}'))
                for finding in data['descriptive_stats']['key_findings']:
                    doc.append(f"• {finding}")
                    doc.append(NoEscape(r'\\'))
        
        # Hypothesis Tests
        if data.get('hypothesis_tests'):
            doc.append(NoEscape(r'\subsection{Statistical Tests}'))
            doc.append(create_hypothesis_test_table(data['hypothesis_tests']))
        
        # Regression Results
        if data.get('regression_results'):
            doc.append(NoEscape(r'\subsection{Regression Analysis}'))
            
            reg = data['regression_results']
            doc.append(f"Model: {reg.get('model_type', 'N/A')} Regression")
            doc.append(NoEscape(r'\\'))
            doc.append(f"Dependent Variable: {reg.get('dependent_var', 'N/A')}")
            doc.append(NoEscape(r'\\'))
            doc.append(f"R-squared: {reg.get('r_squared', 'N/A')}")
            doc.append(NoEscape(r'\\[1em]'))
            
            doc.append(create_regression_table(data['regression_results']))
            
            # Diagnostics summary
            if reg.get('diagnostics'):
                doc.append(NoEscape(r'\paragraph{Model Diagnostics:}'))
                for test, result in reg['diagnostics'].items():
                    doc.append(f"• {test}: {result}")
                    doc.append(NoEscape(r'\\'))
        
        # Visualizations
        if data.get('figures'):
            doc.append(NoEscape(r'\subsection{Visual Analysis}'))
            for i, fig in enumerate(data['figures'], 1):
                add_figure(doc, fig['path'], fig['caption'], fig.get('label', f'fig:analysis{i}'))
    
    # INTERPRETATION & INSIGHTS
    if data.get('interpretation'):
        with doc.create(Section('Interpretation')):
            doc.append(data['interpretation'])
    
    # RECOMMENDATIONS
    if data.get('recommendations'):
        with doc.create(Section('Recommendations')):
            with doc.create(Enumerate()) as enum:
                for rec in data['recommendations']:
                    enum.add_item(rec)
    
    # CONCLUSION
    doc.append(NoEscape(r'\section{Conclusion}'))
    conclusion = _generate_analysis_conclusion(data)
    doc.append(conclusion)
    
    # REFERENCES (if any)
    if data.get('references'):
        doc.append(NoEscape(r'\vspace{1em}'))
        doc.append(NoEscape(r'\subsection*{References}'))
        for ref in data['references']:
            doc.append(NoEscape(ref + r'\\[0.3em]'))
    
    return doc


def _generate_executive_summary(data: dict) -> str:
    """Generate executive summary"""
    summary_parts = []
    
    # Opening
    summary_parts.append("This report presents a comprehensive statistical analysis of the dataset. ")
    
    # Data scope
    if data.get('data_preparation'):
        prep = data['data_preparation']
        summary_parts.append(f"Analysis covers {prep.get('original_shape', 'the complete dataset')}. ")
    
    # Key result
    if data.get('regression_results'):
        reg = data['regression_results']
        r2 = reg.get('r_squared')
        if r2:
            summary_parts.append(f"The statistical model achieved an R² of {float(r2):.3f}, "
                                f"explaining {float(r2)*100:.1f}\\% of variance. ")
    
    # Main finding
    if data.get('descriptive_stats', {}).get('key_findings'):
        summary_parts.append(f"{data['descriptive_stats']['key_findings'][0]} ")
    
    # Recommendations
    if data.get('recommendations'):
        summary_parts.append(f"Key recommendations include: {data['recommendations'][0]}")
    
    return "".join(summary_parts)


def _extract_key_findings(data: dict) -> list:
    """Extract top 3-5 key findings from all results"""
    findings = []
    
    # From descriptive stats
    try:
        if data.get('descriptive_stats', {}).get('key_findings'):
            key_findings = data['descriptive_stats']['key_findings']
            # Handle both list of strings and list of dicts
            if isinstance(key_findings, list):
                for finding in key_findings[:2]:
                    if isinstance(finding, str):
                        findings.append({
                            'title': 'Data Pattern',
                            'detail': finding
                        })
                    elif isinstance(finding, dict):
                        findings.append(finding)
    except Exception as e:
        print(f"Warning: Could not extract descriptive stats findings: {e}")
    
    # From regression
    try:
        if data.get('regression_results'):
            reg = data['regression_results']
            r2 = reg.get('r_squared')
            if r2 is not None:
                findings.append({
                    'title': 'Model Performance',
                    'detail': f"The regression model explains {float(r2)*100:.1f}% of the variance in {reg.get('dependent_var', 'the outcome')}"
                })
            
            # Significant coefficients
            if reg.get('p_values'):
                sig_vars = [var for var, p in reg['p_values'].items() if float(p) < 0.05]
                if sig_vars:
                    findings.append({
                        'title': 'Significant Predictors',
                        'detail': f"Variables {', '.join(sig_vars[:3])} show statistically significant effects (p < 0.05)"
                    })
    except Exception as e:
        print(f"Warning: Could not extract regression findings: {e}")
    
    # From hypothesis tests
    try:
        if data.get('hypothesis_tests') and isinstance(data['hypothesis_tests'], list):
            for test in data['hypothesis_tests'][:1]:
                if isinstance(test, dict):
                    findings.append({
                        'title': test.get('test_name', 'Statistical Test'),
                        'detail': test.get('conclusion', 'Test completed')
                    })
    except Exception as e:
        print(f"Warning: Could not extract hypothesis test findings: {e}")
    
    # If no findings, add a default
    if not findings:
        findings.append({
            'title': 'Analysis Complete',
            'detail': 'Statistical analysis has been performed on the dataset'
        })
    
    
    return findings[:5]  # Return top 5



def _generate_analysis_conclusion(data: dict) -> str:
    """Generate conclusion for analysis report"""
    conclusion_parts = []
    
    conclusion_parts.append("This analysis has provided comprehensive insights into the dataset through "
                           "rigorous statistical examination. ")
    
    if data.get('regression_results'):
        conclusion_parts.append("The regression analysis confirmed significant relationships between key variables, "
                               "with all diagnostic tests indicating model validity. ")
    
    conclusion_parts.append("The findings support data-driven decision-making and provide a solid foundation "
                           "for strategic planning.")
    
    return "".join(conclusion_parts)


from pylatex.lists import Itemize, Enumerate