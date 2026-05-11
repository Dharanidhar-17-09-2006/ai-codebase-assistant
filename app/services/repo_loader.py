import os

IGNORE_DIRS = {"venv", "__pycache__", ".git", "node_modules"}
VALID_EXTENSIONS = {".py", ".js", ".ts", ".cpp"}

def get_code_files(path):
    code_files = []

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if any(file.endswith(ext) for ext in VALID_EXTENSIONS):
                full_path = os.path.join(root, file)
                clean_path = os.path.normpath(full_path)  
                code_files.append(clean_path)

    return code_files