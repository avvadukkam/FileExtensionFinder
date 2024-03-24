import os
import binascii
import tkinter as tk
from tkinter import filedialog

# Dictionary to map file extensions to corresponding values
EXTENSION_MAP = {
    ".pdf": "255044",
    ".mp4": ["6674797069","6674797069"],
    ".3gp": "6674797033",
    ".heic": "6674797068",
    ".jpeg": "ffd8ff",
    ".doc": "d0cf11",
    ".docx": "504b0",
    ".py": "696d70",
    ".txt": ["efbbbf","fffe","feff","fffe", "0efeff"],
    ".zip": "504b0"
}

def find_file_extension(file_path):
    """
    Function to find the file extension of a file based on the first line content.
    """
    with open(file_path, 'rb') as file:  # Open the file in binary mode
        try:
            for i in range(1):
                line = file.readline().strip()
                if line:  # Check if line is not empty
                    hex_data = binascii.hexlify(line)
                    print(hex_data)
                    for ext, hexCodes in EXTENSION_MAP.items():
                        if isinstance(hexCodes, str):
                            hexCodes = [hexCodes]  # Convert single hex code to list for consistency
                        for hexCode in hexCodes:
                            if str(hexCode.lower()) in str(hex_data.lower()):
                                print(ext)
                                return ext
                return ".txt"  # Default to .txt if the extension cannot be determined from the first line
        except UnicodeDecodeError:
            return ""  # Default to .txt if decoding fails
def rename_file_with_extension(file_path, new_extension):
    """
    Function to rename a file with a new extension.
    """
    file_name, _ = os.path.splitext(file_path)
    new_file_name = f"{file_name}{new_extension}"
    os.rename(file_path, new_file_name)
    print(f"File '{file_path}' renamed to '{new_file_name}'")
def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def main():
    # Get folder path from user input
    directory = select_folder()
    if not directory:
        print("No folder selected. Exiting...")
        return

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, filename)):
            # Get the full path of the file
            file_path = os.path.join(directory, filename)

            # Find the file extension based on the first and second non-empty line content
            file_extension = find_file_extension(file_path)

            # Rename the file with the correct extension
            rename_file_with_extension(file_path, file_extension)


if __name__ == "__main__":
    main()