import os

def print_directory_structure(root_dir):
    # List all files and directories in the current directory
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        
        # Check if the item is a file or a directory
        if os.path.isfile(item_path):
            print(f'File: {item}')
        elif os.path.isdir(item_path):
            print(f'Directory: {item}')

# Specify the root directory (current directory)
root_directory = os.getcwd()

# Print the directory structure starting from the root directory
print_directory_structure(root_directory)
