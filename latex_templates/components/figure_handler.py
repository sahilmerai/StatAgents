from pylatex import Figure, NoEscape
import os

def add_figure(doc, image_path: str, caption: str, label: str, width: str = '0.8'):
    """
    Add figure to document.
    
    Args:
        doc: PyLaTeX Document object
        image_path: Path to image file
        caption: Figure caption
        label: Figure label for referencing
        width: Figure width as fraction of textwidth (default 0.8)
    """
    
    # Check if file exists
    if not os.path.exists(image_path):
        doc.append(NoEscape(f'\\textbf{{Figure not found: {image_path}}}'))
        doc.append(NoEscape(r'\\[1em]'))
        return
    
    # Convert to absolute path or relative to output directory
    abs_path = os.path.abspath(image_path)
    
    # Create figure
    with doc.create(Figure(position='H')) as fig:
        fig.add_image(abs_path, width=NoEscape(f'{width}\\textwidth'))
        fig.add_caption(caption)
        fig.append(NoEscape(f'\\label{{{label}}}'))