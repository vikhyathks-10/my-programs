import os
import shutil
folder_path = input("Enter the folder path to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Others": []
}
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        moved = False
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("✅ Files organized successfully.")
