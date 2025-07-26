import os
import config as cfg
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):  # Check if the path is a file
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_dir, 'r') as file:
            content = file.read(cfg.MAX_CHARS)  # Read the file content
            if len(content) == 0:
                return f'Error: File "{file_path}" is empty or could not be read'
          # Return only the first MAX_CHARS characters
    except Exception as e:
        return f"Error reading file: {e}"

    return content[:cfg.MAX_CHARS]



schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents from the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The file to read from, relative to the working directory. If not provided, reads from the working directory itself.",
            ),
        },
    ),
)