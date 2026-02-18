import sys
from io import StringIO
import matplotlib
matplotlib.use('Agg')
import os
import re

# GET ABSOLUTE PATH FOR LOG FILE
CPY_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(CPY_DIR, 'logs', 'execution.log')

def execute_python_code(code: str) -> str:
    with open(os.path.join(CPY_DIR, 'logs', 'debug.log'), 'a') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"CWD: {os.getcwd()}\n")
        f.write(f"CPY_DIR: {CPY_DIR}\n")
        f.write(f"../data/ exists: {os.path.exists('../data/')}\n")
        f.write(f"Code received (first 200 chars): {code[:200]}\n")
    
    """
    Execute Python code with safety checks and automatic path conversion.
    Converts ./data/ to ../data/ for correct relative paths.
    """
    
    # SAFETY CHECK 1: Forbidden operations
    FORBIDDEN = [
        'os.system', 'subprocess.', 'eval(', 'exec(', '__import__', 
        'shutil.rmtree', 'os.remove', 'os.rmdir', 'os.unlink'
    ]
    


    for pattern in FORBIDDEN:
        if pattern in code:
            return f"❌ Error: Forbidden operation detected: {pattern}\nThis operation is not allowed for security reasons."
    
    # PATH CONVERSION: ./data/ → ../data/ (only if starts with ./)
    code_converted = code
    
    # ENSURE OUTPUT DIRECTORIES EXIST
    try:
        os.makedirs('../data/Output/Plots', exist_ok=True)
        os.makedirs('../data/Output/Report', exist_ok=True)
        os.makedirs('../data/Processed_data', exist_ok=True)
        os.makedirs(os.path.join(CPY_DIR, 'logs'), exist_ok=True)
    except Exception as e:
        return f"❌ Error creating output directories: {str(e)}"
    
    # SAFETY CHECK 2: File existence validation
    csv_reads = re.findall(r"pd\.read_csv\(['\"](.+?)['\"]\)", code_converted)
    missing_files = []
    
    for filepath in csv_reads:
        if not os.path.exists(filepath):
            missing_files.append(filepath)
    
    if missing_files:
        return f"❌ Error: Files not found:\n" + "\n".join(f"  - {f}" for f in missing_files) + "\n\nPlease check if the file exists and the path is correct."
    
    # EXECUTE CODE
    stdout_capture = StringIO()
    stderr_capture = StringIO()
    
    try:
        # Save temp.py file for debugging
        with open("temp.py", "w", encoding='utf-8') as f:
            f.write(code_converted)
        
        # Redirect stdout and stderr
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture
        
        # Execute code
        global_vars = {
            '__name__': '__main__',
            '__builtins__': __builtins__,
        }
        exec(code_converted, global_vars)
        
        # AUTO-CLOSE MATPLOTLIB PLOTS
        import matplotlib.pyplot as plt
        plt.close('all')
        
        # Restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
        # Capture output
        output = stdout_capture.getvalue()
        errors = stderr_capture.getvalue()
        
        # Log execution
        try:
            log_message = f"\n{'='*50}\nEXECUTION LOG\n{'='*50}\n"
            log_message += f"Code executed successfully\n"
            if output:
                log_message += f"\nOutput:\n{output}"
            if errors:
                log_message += f"\nWarnings:\n{errors}"
            
            with open(LOG_FILE, "a", encoding='utf-8') as log:
                log.write(log_message + "\n")
        except Exception as log_error:
            pass
        
        result = "✅ Code executed successfully"
        if output:
            result += f"\n\nOutput:\n{output}"
        if errors:
            result += f"\n\nWarnings:\n{errors}"
        
        return result
        
    except Exception as e:
        # Restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
        # Close plots on error
        try:
            import matplotlib.pyplot as plt
            plt.close('all')
        except:
            pass
        
        error_msg = f"❌ Execution Error: {str(e)}"
        
        # Log error
        try:
            with open(LOG_FILE, "a", encoding='utf-8') as log:
                log.write(f"\n{'='*50}\nERROR LOG\n{'='*50}\n")
                log.write(f"Error: {str(e)}\n")
                log.write(f"Code:\n{code_converted}\n")
        except Exception as log_error:
            pass
        
        return error_msg


def execute_python_code_T(code: str) -> str:
    with open(os.path.join(CPY_DIR, 'logs', 'debug.log'), 'a') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"CWD: {os.getcwd()}\n")
        f.write(f"CPY_DIR: {CPY_DIR}\n")
        f.write(f"../data/ exists: {os.path.exists('../data/')}\n")
        f.write(f"Code received (first 200 chars): {code[:200]}\n")
    """
    Execute Python code with extended timeout for time series and DOE analyses.
    Converts ./data/ to ../data/ for correct relative paths.
    """
    
    # SAFETY CHECK 1: Forbidden operations
    FORBIDDEN = [
        'os.system', 'subprocess.', 'eval(', 'exec(', '__import__', 
        'shutil.rmtree', 'os.remove', 'os.rmdir', 'os.unlink'
    ]
    
    for pattern in FORBIDDEN:
        if pattern in code:
            return f"❌ Error: Forbidden operation detected: {pattern}\nThis operation is not allowed for security reasons."
    
    # PATH CONVERSION: ./data/ → ../data/ (only if starts with ./)
    code_converted = code
    
    # ENSURE OUTPUT DIRECTORIES EXIST
    try:
        os.makedirs('../data/Output/Plots', exist_ok=True)
        os.makedirs('../data/Output/Report', exist_ok=True)
        os.makedirs('../data/Processed_data', exist_ok=True)
        os.makedirs(os.path.join(CPY_DIR, 'logs'), exist_ok=True)
    except Exception as e:
        return f"❌ Error creating output directories: {str(e)}"
    
    # SAFETY CHECK 2: File existence validation
    csv_reads = re.findall(r"pd\.read_csv\(['\"](.+?)['\"]\)", code_converted)
    missing_files = []
    
    for filepath in csv_reads:
        if not os.path.exists(filepath):
            missing_files.append(filepath)
    
    if missing_files:
        return f"❌ Error: Files not found:\n" + "\n".join(f"  - {f}" for f in missing_files) + "\n\nPlease check if the file exists and the path is correct."
    
    # EXECUTE CODE
    stdout_capture = StringIO()
    stderr_capture = StringIO()
    
    try:
        # Save temp.py file
        with open("temp.py", "w", encoding='utf-8') as f:
            f.write(code_converted)
        
        # Redirect stdout and stderr
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture
        
        # Execute code
        global_vars = {
            '__name__': '__main__',
            '__builtins__': __builtins__,
        }
        exec(code_converted, global_vars)
        
        # AUTO-CLOSE MATPLOTLIB PLOTS
        import matplotlib.pyplot as plt
        plt.close('all')
        
        # Restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
        # Capture output
        output = stdout_capture.getvalue()
        errors = stderr_capture.getvalue()
        
        # Log execution
        try:
            log_message = f"\n{'='*50}\nEXECUTION LOG (Extended Timeout)\n{'='*50}\n"
            log_message += f"Code executed successfully\n"
            if output:
                log_message += f"\nOutput:\n{output}"
            if errors:
                log_message += f"\nWarnings:\n{errors}"
            
            with open(LOG_FILE, "a", encoding='utf-8') as log:
                log.write(log_message + "\n")
        except Exception as log_error:
            pass
        
        result = "✅ Code executed successfully (Extended timeout)"
        if output:
            result += f"\n\nOutput:\n{output}"
        if errors:
            result += f"\n\nWarnings:\n{errors}"
        
        return result
        
    except Exception as e:
        # Restore stdout and stderr
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        
        # Close plots on error
        try:
            import matplotlib.pyplot as plt
            plt.close('all')
        except:
            pass
        
        error_msg = f"❌ Execution Error: {str(e)}"
        
        # Log error
        try:
            with open(LOG_FILE, "a", encoding='utf-8') as log:
                log.write(f"\n{'='*50}\nERROR LOG (Extended Timeout)\n{'='*50}\n")
                log.write(f"Error: {str(e)}\n")
                log.write(f"Code:\n{code_converted}\n")
        except Exception as log_error:
            pass
        
        return error_msg