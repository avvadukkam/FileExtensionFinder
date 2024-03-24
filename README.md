# File Extension Finder
This Python script reads files in a specified directory, determines their file type based on the content of the first few lines, and renames them with the appropriate file extension.

## Features

- Supports a variety of file types including PDF, MP4, JPEG, DOCX, TXT, and ZIP.
- Uses hex codes from the first few lines to accurately identify file types.
- Provides a simple GUI for selecting the directory containing the files.

## Usage

1. Clone the repository or download the `file_extension_finder.py` script.
2. Ensure you have Python installed on your system.
3. Run the script by executing `python file_extension_finder.py`.
4. Select the folder containing the files when prompted using the GUI.
5. The script will then iterate through each file in the directory, identify its file type, and rename it accordingly.

## Dependencies

- Python 3.x
- tkinter (for GUI)
- binascii (for hex decoding)

## Usage Example

```bash
python file_extension_finder.py
```
Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or bug fixes.
