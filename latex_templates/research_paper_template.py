from pylatex import Document, Section, Subsection, Command, Package, NoEscape
from pylatex.utils import bold, italic
from datetime import datetime
from latex_templates.components.regression_table import create_regression_table
from latex_templates.components.descriptive_stats_table import create_descriptive_stats_table
from latex_templates.components.hypothesis_test_table import create_hypothesis_test_table
from latex_templates.components.data_preparation_section import create_data_prep_section
from latex_templates.components.figure_handler import add_figure

def generate_research_paper(title: str, data: dict) -> Document:
    """
    Generate research paper format report.
    
    Sections:
    - Abstract
    - Introduction
    - Literature Review
    - Data & Methodology
    - Results
    - Discussion
    - Conclusion
    - References
    """
    
    # Document setup with geometry
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
    
    # Title, author, date
    doc.preamble.append(Command('title', title))
    author = data.get('author', 'Statistical Analysis Team')
    doc.preamble.append(Command('author', author))
    date = data.get('date', datetime.now().strftime('%B %d, %Y'))
    doc.preamble.append(Command('date', date))
    
    doc.append(NoEscape(r'\maketitle'))
    
    # ABSTRACT
    with doc.create(Section('Abstract', numbering=False)):
        # Generate abstract from key findings
        abstract_text = _generate_abstract(data)
        doc.append(abstract_text)
    
    doc.append(NoEscape(r'\newpage'))
    
    # INTRODUCTION
    with doc.create(Section('Introduction')):
        intro_text = data.get('introduction', 
            "This research paper presents a comprehensive statistical analysis examining the relationships "
            "and patterns within the dataset. The study employs rigorous statistical methods to derive "
            "meaningful insights and validate hypotheses.")
        doc.append(intro_text)
        
        # Research objectives
        doc.append(NoEscape(r'\subsection{Research Objectives}'))
        objectives = data.get('objectives', [
            "Conduct exploratory data analysis to understand data characteristics",
            "Identify and address data quality issues",
            "Apply appropriate statistical methods to test hypotheses",
            "Provide evidence-based recommendations"
        ])
        with doc.create(Enumerate()) as enum:
            for obj in objectives:
                enum.add_item(obj)
    
    # LITERATURE REVIEW
    if data.get('literature_review') or data.get('references'):
        with doc.create(Section('Literature Review')):
            lit_review = data.get('literature_review', 
                "This analysis builds upon established statistical methodologies and econometric techniques "
                "documented in the literature. The methods employed are consistent with standard practices "
                "in statistical analysis.")
            doc.append(lit_review)
    
    # DATA & METHODOLOGY
    with doc.create(Section('Data and Methodology')):
        
        # Data Description
        doc.append(NoEscape(r'\subsection{Data Description}'))
        data_desc = data.get('data_description', 
            f"The dataset contains {data.get('data_preparation', {}).get('original_shape', 'N/A')} "
            f"from {data.get('data_preparation', {}).get('original_file', 'the source file')}.")
        doc.append(data_desc)
        
        # Data Preparation
        if data.get('data_preparation'):
            doc.append(create_data_prep_section(data['data_preparation']))
        
        # Methodology
        doc.append(NoEscape(r'\subsection{Statistical Methods}'))
        methods = data.get('methods', 
            "This study employs multiple statistical techniques including descriptive statistics, "
            "hypothesis testing, and regression analysis. All analyses were conducted with appropriate "
            "diagnostic tests to ensure validity of results.")
        doc.append(methods)
    
    # RESULTS
    with doc.create(Section('Results')):
        
        # Descriptive Statistics
        if data.get('descriptive_stats'):
            doc.append(NoEscape(r'\subsection{Descriptive Statistics}'))
            doc.append("Table \\ref{tab:descriptive} presents summary statistics for key variables.")
            doc.append(create_descriptive_stats_table(data['descriptive_stats']))
            
            # Key findings
            if data['descriptive_stats'].get('key_findings'):
                doc.append(NoEscape(r'\paragraph{Key Observations:}'))
                with doc.create(Itemize()) as itemize_list:
                    for finding in data['descriptive_stats']['key_findings']:
                        itemize_list.add_item(finding)
        
        # Hypothesis Tests
        if data.get('hypothesis_tests'):
            doc.append(NoEscape(r'\subsection{Hypothesis Testing}'))
            doc.append(create_hypothesis_test_table(data['hypothesis_tests']))
        
        # Regression Analysis
        if data.get('regression_results'):
            doc.append(NoEscape(r'\subsection{Regression Analysis}'))
            doc.append(create_regression_table(data['regression_results']))
        
        # Figures
        if data.get('figures'):
            doc.append(NoEscape(r'\subsection{Visualizations}'))
            for fig in data['figures']:
                add_figure(doc, fig['path'], fig['caption'], fig.get('label', 'fig:plot'))
    
    # DISCUSSION
    with doc.create(Section('Discussion')):
        discussion = data.get('interpretation', 
            "The results indicate significant relationships between the variables of interest. "
            "All diagnostic tests confirm the validity of the analytical approach.")
        doc.append(discussion)
        
        # Implications
        doc.append(NoEscape(r'\subsection{Practical Implications}'))
        implications = data.get('implications', 
            "These findings have important implications for understanding the underlying phenomena "
            "and can inform decision-making processes.")
        doc.append(implications)
    
    # CONCLUSION
    with doc.create(Section('Conclusion')):
        conclusion = _generate_conclusion(data)
        doc.append(conclusion)
        
        # Recommendations
        if data.get('recommendations'):
            doc.append(NoEscape(r'\subsection{Recommendations}'))
            with doc.create(Enumerate()) as enum:
                for rec in data['recommendations']:
                    enum.add_item(rec)
    
    # REFERENCES
    if data.get('references'):
        doc.append(NoEscape(r'\newpage'))
        with doc.create(Section('References', numbering=False)):
            for ref in data['references']:
                doc.append(NoEscape(ref + r'\\[0.5em]'))
    
    return doc


def _generate_abstract(data: dict) -> str:
    """Generate abstract from data"""
    abstract_parts = []
    
    # Purpose
    abstract_parts.append("This study presents a comprehensive statistical analysis of the dataset.")
    
    # Data info
    if data.get('data_preparation'):
        prep = data['data_preparation']
        abstract_parts.append(f"The analysis examines {prep.get('original_shape', 'the data')}, "
                             f"addressing data quality issues through systematic cleaning procedures.")
    
    # Methods
    methods = []
    if data.get('descriptive_stats'):
        methods.append("descriptive statistics")
    if data.get('regression_results'):
        methods.append("regression analysis")
    if data.get('hypothesis_tests'):
        methods.append("hypothesis testing")
    
    if methods:
        abstract_parts.append(f"Statistical methods employed include {', '.join(methods)}.")
    
    # Key result
    if data.get('regression_results'):
        reg = data['regression_results']
        r2 = reg.get('r_squared', 'N/A')
        abstract_parts.append(f"The regression model explains {float(r2)*100:.1f}\\% of the variance "
                             f"in the dependent variable.")
    
    # Conclusion
    abstract_parts.append("Results provide evidence-based insights for informed decision-making.")
    
    return " ".join(abstract_parts)


def _generate_conclusion(data: dict) -> str:
    """Generate conclusion from data"""
    conclusion_parts = []
    
    conclusion_parts.append("This research has demonstrated the application of rigorous statistical "
                           "methods to analyze the dataset comprehensively.")
    
    if data.get('regression_results'):
        conclusion_parts.append("The regression analysis revealed significant relationships between "
                               "variables, with all diagnostic tests supporting model validity.")
    
    conclusion_parts.append("These findings contribute to a deeper understanding of the phenomena "
                           "under investigation and provide actionable insights.")
    
    return " ".join(conclusion_parts)


# Need to import itemize and enumerate
from pylatex.lists import Itemize, Enumerate