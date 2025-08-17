import os

def get_files_info(working_directory, directory="."):
    workdrcty = os.path.join(working_directory, directory)
    output = ""
    
    if not os.path.abspath(workdrcty).startswith(os.path.abspath(working_directory)):
    
         return (f'Error: Cannot list "{workdrcty}" as it is outside the permitted working directory\n')

    if not os.path.isdir(workdrcty):
        return (f'Error: "{workdrcty}" is not a directory\n')
    
    try:
        for item in os.listdir(workdrcty):
            if item.startswith("__") or item.startswith("."):
                continue

            if os.path.isdir(os.path.join(workdrcty, item)):
                output += f" - {item}: file_size={os.path.getsize(os.path.join(workdrcty, item))} bytes, is_dir=True\n"
            else: 
                output += f" - {item}: file_size={os.path.getsize(os.path.join(workdrcty, item))} bytes, is_dir=False\n"
    
        return output
    except Exception as e:
        return f"Error listing files: {e}"