import os
import shutil
from pathlib import Path

# **Note**: Cookiecutter variables are rendered into this script using Jinja.
# The variable values are converted to strings in the context,
# so we compare against the string 'no'.
INCLUDE_MKDOCS_DOCS = '{{ cookiecutter.include_mkdocs_docs }}'
WINDOWS_DEVELOPMENT = '{{ cookiecutter.developing_on_windows }}'

MKDOCS_PATHS_TO_REMOVE = [
    'mkdocs.yml',
    'docs/',
]

WINDOWS_DEVELOPMENT_PATHS_TO_REMOVE = [
    'tasks.py',
]

def remove_mkdocs_files():
    """Removes MkDocs documentation structure if the user opted out."""
    
    # The hook's working directory is the root of the generated project.
    project_root = Path.cwd() 
    
    print(f"\n--- Post Generation Hook: Removing unnecessary files ---")
    
    # Check if the user chose to exclude documentation
    if INCLUDE_MKDOCS_DOCS.lower() == 'no':
        print(f"Documentation requested: {INCLUDE_MKDOCS_DOCS}. Removing MkDocs structure...")

        for path_str in MKDOCS_PATHS_TO_REMOVE:
            full_path = project_root / path_str
            
            if full_path.exists():
                if full_path.is_dir():
                    shutil.rmtree(full_path)
                    print(f"  - Removed directory: {path_str}")
                else:
                    os.remove(full_path)
                    print(f"  - Removed file: {path_str}")
            else:
                # This can happen if the path is inside a conditional folder
                print(f"  - Warning: Path not found (already removed or not generated): {path_str}")
    else:
        print(f"Documentation requested: {INCLUDE_MKDOCS_DOCS}. Keeping MkDocs structure.")
    
    print(f"----------------------------------------------------------\n")

def remove_windows_dev_files():
    # The hook's working directory is the root of the generated project.
    project_root = Path.cwd() 
    
    print(f"\n--- Post Generation Hook: Removing unnecessary Windows development files ---")

    if WINDOWS_DEVELOPMENT.lower() == 'no':
        print(f"Removing unneeded Windows development files...")

        for path_str in WINDOWS_DEVELOPMENT_PATHS_TO_REMOVE:
            full_path = project_root / path_str
            
            if full_path.exists():
                if full_path.is_dir():
                    shutil.rmtree(full_path)
                    print(f"  - Removed directory: {path_str}")
                else:
                    os.remove(full_path)
                    print(f"  - Removed file: {path_str}")
            else:
                # This can happen if the path is inside a conditional folder
                print(f"  - Warning: Path not found (already removed or not generated): {path_str}")
    else:
        print(f"Keeping Windows development files.")

    print(f"----------------------------------------------------------\n")


if __name__ == '__main__':
    # Use 'yes' and 'no' as strings, and lower() to handle case variations
    if INCLUDE_MKDOCS_DOCS.lower() == 'no':
        remove_mkdocs_files()

    if WINDOWS_DEVELOPMENT.lower() == 'no':
        remove_windows_dev_files()