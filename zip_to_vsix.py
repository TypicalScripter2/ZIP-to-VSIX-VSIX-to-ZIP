import os
import sys

def zip_to_vsix(file_path):
    # Normalize the path
    file_path = os.path.abspath(file_path.strip('"').strip("'"))

    if not os.path.isfile(file_path):
        print(f"❌ File does not exist: {file_path}")
        return

    base, ext = os.path.splitext(file_path)

    if ext.lower() == ".zip":
        new_file = base + ".vsix"
        os.rename(file_path, new_file)
        print(f"✅ Converted ZIP → VSIX: {new_file}")
    elif ext.lower() == ".vsix":
        new_file = base + ".zip"
        os.rename(file_path, new_file)
        print(f"✅ Converted VSIX → ZIP: {new_file}")
    else:
        print("❌ Unsupported file type. Use a .zip or .vsix file.")

if len(sys.argv) > 1:
    # Drag-and-drop support
    zip_to_vsix(sys.argv[1])
else:
    # Manual path input
    file_path = input("Enter the full path to your .zip or .vsix file: ")
    zip_to_vsix(file_path)