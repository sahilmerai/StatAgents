from pylatex import Document, Section, Subsection, Subsubsection, Command, Package, NoEscape
from pylatex.utils import bold, italic, verbatim
from datetime import datetime
from latex_templates.components.regression_table import create_regression_table
from latex_templates.components.descriptive_stats_table import create_descriptive_stats_table
from latex_templates.components.hypothesis_test_table import create_hypothesis_test_table
from latex_templates.components.data_preparation_section import create_data_prep_section
from latex_templates.components.figure_handler import add_figure

def generate_technical_doc(title: str, data: dict) -> Document:
    """
    Generate technical documentation format.
    
    Sections:
    - Overview
    - Data Specifications
    - Methods & Procedures
    - Results & Validation
    - Technical Notes
    - Appendices
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
    doc.packages.append(Package('listings'))  # For code
    doc.packages.append(Package('xcolor'))
    
    # Code listing settings
    doc.preamble.append(NoEscape(r'''
\lstset{
    basicstyle=\ttfamily\small,
    breaklines=true,
    frame=single,
    backgroundcolor=\color{gray!10}
}
'''))
    
    # Title, author, date
    doc.preamble.append(Command('title', NoEscape(r'\texttt{' + title + '}')))
    author = data.get('author', 'Technical Team')
    doc.preamble.append(Command('author', author))
    date = data.get('date', datetime.now().strftime('%B %d, %Y'))
    doc.preamble.append(Command('date', date))
    
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\tableofcontents'))
    doc.append(NoEscape(r'\newpage'))
    
    # OVERVIEW
    with doc.create(Section('Overview')):
        doc.append(NoEscape(r'\subsection{Purpose}'))
        purpose = data.get('purpose', 
            "This technical documentation provides comprehensive details of the statistical analysis "
            "procedures, methodologies, and results for reproducibility and audit purposes.")
        doc.append(purpose)
        
        doc.append(NoEscape(r'\subsection{Scope}'))
        scope = data.get('scope',
            "This document covers data specifications, preprocessing procedures, statistical methods, "
            "validation results, and technical implementation details.")
        doc.append(scope)
        
        doc.append(NoEscape(r'\subsection{Document Version}'))
        version = data.get('version', '1.0')
        doc.append(f"Version: {version}")
        doc.append(NoEscape(r'\\'))
        doc.append(f"Date: {date}")
    
    # DATA SPECIFICATIONS
    with doc.create(Section('Data Specifications')):
        
        doc.append(NoEscape(r'\subsection{Source Data}'))
        if data.get('data_preparation'):
            prep = data['data_preparation']
            
            # Create specifications table
            doc.append(NoEscape(r'\begin{table}[H]'))
            doc.append(NoEscape(r'\centering'))
            doc.append(NoEscape(r'\begin{tabular}{ll}'))
            doc.append(NoEscape(r'\toprule'))
            doc.append(NoEscape(r'\textbf{Attribute} & \textbf{Value} \\'))
            doc.append(NoEscape(r'\midrule'))
            doc.append(NoEscape(f"Source File & \\texttt{{{prep.get('original_file', 'N/A')}}} \\\\"))
            doc.append(NoEscape(f"Dimensions & {prep.get('original_shape', 'N/A')} \\\\"))
            doc.append(NoEscape(f"Data Type & {data.get('data_type', 'Cross-sectional')} \\\\"))
            doc.append(NoEscape(r'\bottomrule'))
            doc.append(NoEscape(r'\end{tabular}'))
            doc.append(NoEscape(r'\caption{Data Source Specifications}'))
            doc.append(NoEscape(r'\end{table}'))
        
        # Data dictionary
        doc.append(NoEscape(r'\subsection{Variable Descriptions}'))
        if data.get('variable_descriptions'):
            doc.append(NoEscape(r'\begin{table}[H]'))
            doc.append(NoEscape(r'\centering'))
            doc.append(NoEscape(r'\begin{tabular}{lll}'))
            doc.append(NoEscape(r'\toprule'))
            doc.append(NoEscape(r'\textbf{Variable} & \textbf{Type} & \textbf{Description} \\'))
            doc.append(NoEscape(r'\midrule'))
            for var in data['variable_descriptions']:
                doc.append(NoEscape(f"{var['name']} & {var['type']} & {var['description']} \\\\"))
            doc.append(NoEscape(r'\bottomrule'))
            doc.append(NoEscape(r'\end{tabular}'))
            doc.append(NoEscape(r'\caption{Variable Dictionary}'))
            doc.append(NoEscape(r'\end{table}'))
    
    # METHODS & PROCEDURES
    with doc.create(Section('Methods and Procedures')):
        
        # Data preprocessing
        doc.append(NoEscape(r'\subsection{Data Preprocessing}'))
        if data.get('data_preparation'):
            doc.append(create_data_prep_section(data['data_preparation']))
            
            # Processing code (if available)
            if data['data_preparation'].get('processing_code'):
                doc.append(NoEscape(r'\subsubsection{Implementation Code}'))
                doc.append(NoEscape(r'\begin{lstlisting}[language=Python]'))
                doc.append(data['data_preparation']['processing_code'])
                doc.append(NoEscape(r'\end{lstlisting}'))
        
        # Statistical methods
        doc.append(NoEscape(r'\subsection{Statistical Methods}'))
        
        # Descriptive statistics method
        if data.get('descriptive_stats'):
            doc.append(NoEscape(r'\subsubsection{Descriptive Statistics}'))
            doc.append("Computed summary statistics including measures of central tendency (mean, median, mode), "
                      "dispersion (standard deviation, variance, range), and distribution shape (skewness, kurtosis). "
                      "Outlier detection performed using IQR method (Q1 - 1.5×IQR, Q3 + 1.5×IQR).")
        
        # Hypothesis testing method
        if data.get('hypothesis_tests'):
            doc.append(NoEscape(r'\subsubsection{Hypothesis Testing}'))
            doc.append("Statistical tests conducted at α = 0.05 significance level. "
                      "Null hypotheses tested against appropriate alternative hypotheses.")
        
        # Regression method
        if data.get('regression_results'):
            doc.append(NoEscape(r'\subsubsection{Regression Analysis}'))
            reg = data['regression_results']
            doc.append(f"Estimation Method: {reg.get('model_type', 'OLS')}")
            doc.append(NoEscape(r'\\'))
            doc.append("Model Specification:")
            doc.append(NoEscape(r'\begin{equation}'))
            
            # Build equation
            dep_var = reg.get('dependent_var', 'Y')
            indep_vars = reg.get('independent_vars', [])
            equation = f"{dep_var} = \\beta_0"
            for i, var in Enumerate(indep_vars, 1):
                equation += f" + \\beta_{{{i}}} {var}"
            equation += " + \\epsilon"
            doc.append(NoEscape(equation))
            doc.append(NoEscape(r'\end{equation}'))
    
    # RESULTS & VALIDATION
    with doc.create(Section('Results and Validation')):
        
        # Descriptive results
        if data.get('descriptive_stats'):
            doc.append(NoEscape(r'\subsection{Descriptive Statistics Results}'))
            doc.append(create_descriptive_stats_table(data['descriptive_stats']))
        
        # Test results
        if data.get('hypothesis_tests'):
            doc.append(NoEscape(r'\subsection{Hypothesis Test Results}'))
            doc.append(create_hypothesis_test_table(data['hypothesis_tests']))
        
        # Regression results
        if data.get('regression_results'):
            doc.append(NoEscape(r'\subsection{Regression Results}'))
            doc.append(create_regression_table(data['regression_results']))
            
            # Diagnostics
            if data['regression_results'].get('diagnostics'):
                doc.append(NoEscape(r'\subsection{Diagnostic Tests}'))
                doc.append(NoEscape(r'\begin{table}[H]'))
                doc.append(NoEscape(r'\centering'))
                doc.append(NoEscape(r'\begin{tabular}{ll}'))
                doc.append(NoEscape(r'\toprule'))
                doc.append(NoEscape(r'\textbf{Diagnostic Test} & \textbf{Result} \\'))
                doc.append(NoEscape(r'\midrule'))
                for test, result in data['regression_results']['diagnostics'].items():
                    doc.append(NoEscape(f"{test} & {result} \\\\"))
                doc.append(NoEscape(r'\bottomrule'))
                doc.append(NoEscape(r'\end{tabular}'))
                doc.append(NoEscape(r'\caption{Regression Diagnostic Tests}'))
                doc.append(NoEscape(r'\end{table}'))
        
        # Figures
        if data.get('figures'):
            doc.append(NoEscape(r'\subsection{Visual Validation}'))
            for fig in data['figures']:
                add_figure(doc, fig['path'], fig['caption'], fig.get('label', 'fig:result'))
    
    # TECHNICAL NOTES
    with doc.create(Section('Technical Notes')):
        
        doc.append(NoEscape(r'\subsection{Software Environment}'))
        software_info = data.get('software_info', {
            'Python': '3.11',
            'pandas': '2.1.4',
            'statsmodels': '0.14.1',
            'scikit-learn': '1.4.0'
        })
        doc.append(NoEscape(r'\begin{itemize}'))
        for software, version in software_info.items():
            doc.append(NoEscape(f"\\item \\texttt{{{software}}}: {version}"))
        doc.append(NoEscape(r'\end{itemize}'))
        
        doc.append(NoEscape(r'\subsection{Computational Details}'))
        comp_details = data.get('computational_details',
            "All computations performed using standard numerical precision. "
            "Random seed set for reproducibility where applicable.")
        doc.append(comp_details)
        
        doc.append(NoEscape(r'\subsection{Limitations}'))
        limitations = data.get('limitations', [
            "Results are specific to the dataset analyzed",
            "Causal interpretation requires additional assumptions",
            "Generalization beyond sample requires careful consideration"
        ])
        doc.append(NoEscape(r'\begin{itemize}'))
        for limitation in limitations:
            doc.append(NoEscape(f"\\item {limitation}"))
        doc.append(NoEscape(r'\end{itemize}'))
    
    # APPENDICES
    doc.append(NoEscape(r'\appendix'))
    
    # Appendix A: Full processing report
    if data.get('data_preparation', {}).get('processing_report_path'):
        doc.append(NoEscape(r'\section{Data Processing Report}'))
        report_path = data['data_preparation']['processing_report_path']
        doc.append(f"Complete processing report available at:")
        doc.append(NoEscape(r'\\'))
        doc.append(NoEscape(f"\\texttt{{{report_path}}}"))
    
    # Appendix B: Additional figures
    if len(data.get('figures', [])) > 3:
        doc.append(NoEscape(r'\section{Additional Visualizations}'))
        for fig in data['figures'][3:]:
            add_figure(doc, fig['path'], fig['caption'], fig.get('label', 'fig:appendix'))
    
    return doc


from pylatex.lists import Itemize, Enumerate