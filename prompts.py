# utils.py or prompts.py
import os
def load_prompt(filename: str) -> str:
    """Load system prompt from text file"""
    prompt_dir = r"F:\Project work\Cafe Restaurant Analysis\Agents\Agents System prompt"
    file_path = os.path.join(prompt_dir, filename)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading prompt {filename}: {str(e)}")