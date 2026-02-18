from pylatex import Table, Tabular, NoEscape, MultiColumn

def create_hypothesis_test_table(hypothesis_tests: list) -> Table:
    """
    Create hypothesis testing results table.
    
    Args:
        hypothesis_tests: List of dicts, each with:
            - test_name: str
            - variable: str (optional)
            - statistic: float
            - p_value: float
            - conclusion: str
    
    Returns:
        PyLaTeX Table object
    """
    
    table = Table(position='H')
    
    # Column format: Test, Variable, Statistic, P-value, Conclusion
    col_format = 'lllll'
    
    with table.create(Tabular(col_format)) as tabular:
        # Title
        tabular.add_hline()
        tabular.add_row([
            MultiColumn(5, align='c', data=NoEscape(r'\textbf{Hypothesis Testing Results}'))
        ])
        tabular.add_hline()
        
        # Header
        tabular.add_row([
            NoEscape(r'\textbf{Test}'),
            NoEscape(r'\textbf{Variable}'),
            NoEscape(r'\textbf{Statistic}'),
            NoEscape(r'\textbf{P-value}'),
            NoEscape(r'\textbf{Conclusion}')
        ])
        tabular.add_hline()
        
        # Test results
        for test in hypothesis_tests:
            test_name = test.get('test_name', 'N/A')
            variable = test.get('variable', '-')
            statistic = test.get('statistic', 0)
            p_value = test.get('p_value', 1)
            conclusion = test.get('conclusion', 'N/A')
            
            # Format p-value
            if p_value < 0.001:
                p_str = '<0.001'
            else:
                p_str = f'{p_value:.3f}'
            
            # Add significance indicator
            if p_value < 0.05:
                conclusion_str = NoEscape(f'{conclusion} \\textbf{{*}}')
            else:
                conclusion_str = conclusion
            
            tabular.add_row([
                test_name,
                variable,
                f'{statistic:.4f}',
                p_str,
                conclusion_str
            ])
        
        tabular.add_hline()
        
        # Significance note
        tabular.add_row([
            MultiColumn(5, align='l', 
                       data=NoEscape(r'\multicolumn{5}{l}{\footnotesize * Significant at $\alpha = 0.05$ level}'))
        ])
        tabular.add_hline()
    
    table.add_caption('Statistical Hypothesis Tests')
    table.append(NoEscape(r'\label{tab:hypothesis}'))
    
    return table