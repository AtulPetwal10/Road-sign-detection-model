import os

def rename_jpg_files_in_folder(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter out non-jpg files and non-file items
    jpg_files = [f for f in files if f.lower().endswith('.jpg') and os.path.isfile(os.path.join(folder_path, f))]

    # Loop through the jpg files and rename them
    for index, file in enumerate(jpg_files, start=1):
        new_name = f"{index}.jpg"  # New name as a number with .jpg extension
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

# Specify the folder path
folder_path = "./"  # Replace with the actual folder path
rename_jpg_files_in_folder(folder_path)
