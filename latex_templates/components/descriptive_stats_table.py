from pylatex import Table, Tabular, NoEscape, MultiColumn

def create_descriptive_stats_table(descriptive_data: dict) -> Table:
    """
    Create descriptive statistics table.
    
    Args:
        descriptive_data: Dict with 'summary_table' containing:
            - Variable: list of variable names
            - Mean: list of means
            - Std: list of standard deviations
            - Min: list of minimums
            - Max: list of maximums
            - (optional) Median, Q1, Q3, etc.
    
    Returns:
        PyLaTeX Table object
    """
    
    table = Table(position='H')
    
    summary = descriptive_data.get('summary_table', {})
    
    # Get variables and available statistics
    variables = summary.get('Variable', [])
    
    # Determine which statistics are available
    available_stats = []
    stat_columns = ['Mean', 'Median', 'Std', 'Min', 'Q1', 'Q3', 'Max', 'Skewness', 'Kurtosis']
    
    for stat in stat_columns:
        if stat in summary:
            available_stats.append(stat)
    
    # Create column format
    n_cols = 1 + len(available_stats)  # Variable + statistics
    col_format = 'l' + 'r' * len(available_stats)
    
    with table.create(Tabular(col_format)) as tabular:
        # Title
        tabular.add_hline()
        tabular.add_row([
            MultiColumn(n_cols, align='c', data=NoEscape(r'\textbf{Descriptive Statistics}'))
        ])
        tabular.add_hline()
        
        # Header row
        header = [NoEscape(r'\textbf{Variable}')]
        for stat in available_stats:
            header.append(NoEscape(f'\\textbf{{{stat}}}'))
        tabular.add_row(header)
        tabular.add_hline()
        
        # Data rows
        for i, var in enumerate(variables):
            row = [var]
            for stat in available_stats:
                value = summary[stat][i]
                if isinstance(value, (int, float)):
                    row.append(f'{value:.3f}')
                else:
                    row.append(str(value))
            tabular.add_row(row)
        
        tabular.add_hline()
    
    table.add_caption('Descriptive Statistics Summary')
    table.append(NoEscape(r'\label{tab:descriptive}'))
    
    return table