from pylatex import Table, Tabular, NoEscape, MultiColumn

def create_regression_table(regression_data: dict) -> Table:
    """
    Create professional regression results table.
    
    Args:
        regression_data: Dict with keys:
            - model_type: str
            - dependent_var: str
            - independent_vars: list
            - coefficients: dict
            - std_errors: dict
            - p_values: dict
            - r_squared: float
            - adj_r_squared: float
            - observations: int (optional)
    
    Returns:
        PyLaTeX Table object
    """
    
    table = Table(position='H')
    
    # Get data
    model_type = regression_data.get('model_type', 'OLS')
    dep_var = regression_data.get('dependent_var', 'Y')
    indep_vars = regression_data.get('independent_vars', [])
    coefficients = regression_data.get('coefficients', {})
    std_errors = regression_data.get('std_errors', {})
    p_values = regression_data.get('p_values', {})
    r_squared = regression_data.get('r_squared', None)
    adj_r_squared = regression_data.get('adj_r_squared', None)
    n_obs = regression_data.get('observations', None)
    
    # Create tabular
    n_cols = 4  # Variable, Coefficient, Std Error, P-value
    col_format = 'l' + 'r' * (n_cols - 1)
    
    with table.create(Tabular(col_format)) as tabular:
        # Title row
        tabular.add_hline()
        tabular.add_row([
            MultiColumn(n_cols, align='c', data=NoEscape(f'\\textbf{{{model_type} Regression Results}}'))
        ])
        tabular.add_hline()
        
        # Dependent variable
        tabular.add_row([
            MultiColumn(n_cols, align='l', data=NoEscape(f'Dependent Variable: \\textit{{{dep_var}}}'))
        ])
        tabular.add_hline()
        
        # Header row
        tabular.add_row([
            NoEscape(r'\textbf{Variable}'),
            NoEscape(r'\textbf{Coefficient}'),
            NoEscape(r'\textbf{Std. Error}'),
            NoEscape(r'\textbf{P-value}')
        ])
        tabular.add_hline()
        
        # Intercept (if present)
        if 'Intercept' in coefficients or 'const' in coefficients:
            intercept_key = 'Intercept' if 'Intercept' in coefficients else 'const'
            coef = coefficients.get(intercept_key, 0)
            se = std_errors.get(intercept_key, 0)
            pval = p_values.get(intercept_key, 1)
            
            significance = _get_significance_stars(pval)
            
            tabular.add_row([
                'Intercept',
                f'{coef:.4f}{significance}',
                f'({se:.4f})',
                _format_pvalue(pval)
            ])
        
        # Independent variables
        for var in indep_vars:
            coef = coefficients.get(var, 0)
            se = std_errors.get(var, 0)
            pval = p_values.get(var, 1)
            
            significance = _get_significance_stars(pval)
            
            tabular.add_row([
                var,
                f'{coef:.4f}{significance}',
                f'({se:.4f})',
                _format_pvalue(pval)
            ])
        
        tabular.add_hline()
        
        # Model statistics
        if n_obs:
            tabular.add_row([
                'Observations',
                MultiColumn(n_cols - 1, align='r', data=str(n_obs))
            ])
        
        if r_squared is not None:
            tabular.add_row([
                NoEscape(r'R$^2$'),
                MultiColumn(n_cols - 1, align='r', data=f'{r_squared:.4f}')
            ])
        
        if adj_r_squared is not None:
            tabular.add_row([
                NoEscape(r'Adjusted R$^2$'),
                MultiColumn(n_cols - 1, align='r', data=f'{adj_r_squared:.4f}')
            ])
        
        tabular.add_hline()
        
        # Significance note
        tabular.add_row([
            MultiColumn(n_cols, align='l', 
                       data=NoEscape(r'\multicolumn{4}{l}{\footnotesize Significance: *** p<0.01, ** p<0.05, * p<0.10}'))
        ])
        tabular.add_hline()
    
    table.add_caption(f'{model_type} Regression Results')
    table.append(NoEscape(r'\label{tab:regression}'))
    
    return table


def _get_significance_stars(p_value: float) -> str:
    """Return significance stars based on p-value"""
    if p_value < 0.01:
        return '***'
    elif p_value < 0.05:
        return '**'
    elif p_value < 0.10:
        return '*'
    else:
        return ''


def _format_pvalue(p_value: float) -> str:
    """Format p-value for display"""
    if p_value < 0.001:
        return '<0.001'
    else:
        return f'{p_value:.3f}'