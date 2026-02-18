from pylatex import Subsection, NoEscape, Tabular, Table
from pylatex import Subsection, NoEscape, Tabular, Table

def create_data_prep_section(prep_data: dict) -> list:
    """
    Create data preparation subsection content.
    
    Args:
        prep_data: Dict with:
            - original_file: str
            - original_shape: str
            - issues_detected: list
            - cleaning_actions: list
            - final_shape: str
    
    Returns:
        List of PyLaTeX elements to append
    """
    
    elements = []
    
    # Subsection
    elements.append(NoEscape(r'\subsection{Data Preparation}'))
    
    # Original data info
    elements.append(NoEscape(r'\subsubsection{Original Data}'))
    elements.append(f"Source: \\texttt{{{prep_data.get('original_file', 'N/A')}}}")
    elements.append(NoEscape(r'\\'))
    elements.append(f"Dimensions: {prep_data.get('original_shape', 'N/A')}")
    elements.append(NoEscape(r'\\[0.5em]'))
    
    # Data quality issues
    if prep_data.get('issues_detected'):
        elements.append(NoEscape(r'\subsubsection{Data Quality Issues Identified}'))
        elements.append(NoEscape(r'\begin{itemize}'))
        for issue in prep_data['issues_detected']:
            elements.append(NoEscape(f'\\item {issue}'))
        elements.append(NoEscape(r'\end{itemize}'))
    
    # Cleaning actions
    if prep_data.get('cleaning_actions'):
        elements.append(NoEscape(r'\subsubsection{Data Cleaning Procedures}'))
        elements.append(NoEscape(r'\begin{Enumerate}'))
        for action in prep_data['cleaning_actions']:
            elements.append(NoEscape(f'\\item {action}'))
        elements.append(NoEscape(r'\end{Enumerate}'))
    
    # Final data
    elements.append(NoEscape(r'\subsubsection{Processed Data}'))
    elements.append(f"Final Dimensions: {prep_data.get('final_shape', 'N/A')}")
    elements.append(NoEscape(r'\\'))
    elements.append("Data Quality: Clean and ready for analysis")
    elements.append(NoEscape(r'\\[1em]'))
    
    return elements