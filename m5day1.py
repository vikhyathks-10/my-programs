# 🔹 DAY 1 - OS MODULE BASICS

import os


# 🔹 1. Get Current Working Directory
print("\n--- Current Working Directory ---")
print(os.getcwd())


# 🔹 2. Change Directory
# Example: Change to a folder path
# ⚠️ Change the path according to your system

# os.chdir("C:/Users/YourName/Documents")

# print("\n--- After Changing Directory ---")
# print(os.getcwd())


# 🔹 3. Create Folder
folder_name = "DemoFolder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("\nFolder Created")
else:
    print("\nFolder Already Exists")


# 🔹 4. Delete Folder
# Folder must be empty to delete

delete_folder = "TempFolder"

# Create temp folder first
if not os.path.exists(delete_folder):
    os.mkdir(delete_folder)

# Delete folder
os.rmdir(delete_folder)
print("TempFolder Deleted")


# 🔹 5. List Files in Directory
print("\n--- Files & Folders in Current Directory ---")

files = os.listdir()

for file in files:
    print(file)