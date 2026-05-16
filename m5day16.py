# 🔹 DAY 16 - FOLDER AUTOMATION

import os
import shutil


# 🔹 1. Empty Folder Cleaner

def remove_empty_folders(path):

    print("\n--- Empty Folder Cleaner ---")

    for folder, subfolders, files in os.walk(path, topdown=False):

        if not os.listdir(folder):
            os.rmdir(folder)
            print("Removed Empty Folder:", folder)


# 🔹 2. Folder Size Checker

def folder_size(path):

    print("\n--- Folder Size Checker ---")

    total_size = 0

    for folder, subfolders, files in os.walk(path):

        for file in files:

            file_path = os.path.join(folder, file)

            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)

    print("Total Folder Size:",
          round(total_size / 1024, 2), "KB")


# 🔹 3. Auto Folder Creator

def create_folders(base_name, count):

    print("\n--- Auto Folder Creator ---")

    for i in range(1, count + 1):

        folder_name = f"{base_name}_{i}"

        if not os.path.exists(folder_name):
            os.mkdir(folder_name)

    print(count, "Folders Created")


# 🔹 4. Folder Organizer

def organize_by_extension(path):

    print("\n--- Folder Organizer ---")

    for file in os.listdir(path):

        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1][1:]

            if ext == "":
                ext = "others"

            folder_name = ext.upper() + "_Files"

            target_folder = os.path.join(path, folder_name)

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            shutil.move(file_path,
                        os.path.join(target_folder, file))

    print("Folder Organized")


# 🔹 5. Temporary File Remover

def remove_temp_files(path):

    print("\n--- Temporary File Remover ---")

    removed = 0

    for folder, subfolders, files in os.walk(path):

        for file in files:

            if file.endswith(".tmp") or file.endswith(".temp"):

                file_path = os.path.join(folder, file)

                os.remove(file_path)

                removed += 1

                print("Removed:", file)

    print("Total Temp Files Removed:", removed)


# 🔹 MAIN PROGRAM

path = "."


# ⚠️ Uncomment carefully when testing

# remove_empty_folders(path)

folder_size(path)

create_folders("DemoFolder", 3)

# organize_by_extension(path)


# Create sample temp files
with open("sample.tmp", "w") as f:
    f.write("temporary data")

with open("cache.temp", "w") as f:
    f.write("cache file")


remove_temp_files(path)