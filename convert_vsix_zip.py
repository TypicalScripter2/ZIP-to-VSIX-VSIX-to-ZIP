import os

def convert_file(file_path):
    # Remove quotes if user adds them
    file_path = file_path.strip('"').strip("'")
    
    if not os.path.isfile(file_path):
        print("❌ File does not exist. Please check the path.")
        return
    
    base, ext = os.path.splitext(file_path)
    
    if ext.lower() == ".vsix":
        new_file = base + ".zip"
        os.rename(file_path, new_file)
        print(f"✅ Converted VSIX → ZIP: {new_file}")
    elif ext.lower() == ".zip":
        new_file = base + ".vsix"
        os.rename(file_path, new_file)
        print(f"✅ Converted ZIP → VSIX: {new_file}")
    else:
        print("❌ Unsupported file type. Use a .vsix or .zip file.")

# Prompt the user for the file path
file_path = input("Enter the full path to your .vsix or .zip file: ")
convert_file(file_path)