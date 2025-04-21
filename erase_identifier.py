import os

def delete_zone_identifier_files(root_folder):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('Zone.Identifier'):
                file_path = os.path.join(dirpath, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    folder_to_scan = r"./"  # <- Replace with your actual path
    delete_zone_identifier_files(folder_to_scan)