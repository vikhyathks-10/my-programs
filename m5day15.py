# 🔹 DAY 15 - FILE AUTOMATION

import os
import shutil
import hashlib


# 🔹 1. Bulk File Renamer

def bulk_rename(folder_path):

    print("\n--- Bulk File Renamer ---")

    files = os.listdir(folder_path)

    count = 1

    for file in files:

        old_path = os.path.join(folder_path, file)

        if os.path.isfile(old_path):

            ext = os.path.splitext(file)[1]

            new_name = f"file_{count}{ext}"

            new_path = os.path.join(folder_path, new_name)

            os.rename(old_path, new_path)

            count += 1

    print("Files Renamed Successfully")


# 🔹 2. File Extension Sorter

def extension_sorter(folder_path):

    print("\n--- File Extension Sorter ---")

    files = os.listdir(folder_path)

    for file in files:

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            ext = os.path.splitext(file)[1][1:]

            if ext == "":
                ext = "others"

            folder_name = ext.upper() + "_Files"

            target_folder = os.path.join(folder_path, folder_name)

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            shutil.move(file_path,
                        os.path.join(target_folder, file))

    print("Files Sorted")


# 🔹 3. File Backup Creator

def create_backup(source_file):

    print("\n--- File Backup Creator ---")

    backup_file = source_file + ".backup"

    shutil.copy(source_file, backup_file)

    print("Backup Created:", backup_file)


# 🔹 4. File Copier

def copy_file(source, destination):

    print("\n--- File Copier ---")

    shutil.copy(source, destination)

    print("File Copied Successfully")


# 🔹 5. Duplicate File Finder

def file_hash(filepath):

    hasher = hashlib.md5()

    with open(filepath, "rb") as f:

        while chunk := f.read(4096):
            hasher.update(chunk)

    return hasher.hexdigest()


def find_duplicates(folder_path):

    print("\n--- Duplicate File Finder ---")

    hashes = {}

    duplicates = []

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            h = file_hash(file_path)

            if h in hashes:
                duplicates.append(file)
            else:
                hashes[h] = file

    return duplicates


# 🔹 MAIN PROGRAM

folder = "."


# ⚠️ Uncomment carefully when testing

# bulk_rename(folder)

# extension_sorter(folder)


# Create sample file
with open("sample.txt", "w") as f:
    f.write("Hello Python")


# Backup creator
create_backup("sample.txt")


# File copier
copy_file("sample.txt", "copied_sample.txt")


# Duplicate finder
print(find_duplicates(folder))