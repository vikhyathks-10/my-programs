import os

folder_path = input("Enter folder path: ")
files = os.listdir(folder_path)

for index, filename in enumerate(files, start=1):
    name, extension = os.path.splitext(filename)
    new_name = f"file{index}{extension}"
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_name)
    os.rename(old_file, new_file)
    print(f"Renamed '{filename}' to '{new_name}'")

print("Renaming complete!")
