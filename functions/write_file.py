import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_dir):
        return f'Error: Cannot write to a directory: "{file_path}"'
    if not os.path.exists(os.path.dirname(target_dir)):
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)


    try:
        with open(target_dir, 'w') as file:
            file.write(content)
    except Exception as e:
        return f"Error writing file: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'