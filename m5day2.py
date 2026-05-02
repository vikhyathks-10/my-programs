# 🔹 DAY 2 - ADVANCED OS MODULE

import os


# 🔹 1. Rename File

# Create sample file
with open("old_file.txt", "w") as f:
    f.write("Hello")

# Rename file
os.rename("old_file.txt", "new_file.txt")
print("\nFile Renamed Successfully")


# 🔹 2. Check File Existence

file_name = "new_file.txt"

print("\n--- File Existence Check ---")

if os.path.exists(file_name):
    print(file_name, "exists")
else:
    print(file_name, "does not exist")


# 🔹 3. Get File Size

print("\n--- File Size ---")

size = os.path.getsize(file_name)

print("File Size:", size, "bytes")


# 🔹 4. Traverse Folders using os.walk()

print("\n--- Folder Traversal ---")

for folder, subfolders, files in os.walk("."):
    print("\nCurrent Folder:", folder)

    print("Subfolders:")
    for sub in subfolders:
        print("  ", sub)

    print("Files:")
    for file in files:
        print("  ", file)


# 🔹 5. Count Files in Folder

print("\n--- File Count ---")

count = 0

for item in os.listdir("."):
    if os.path.isfile(item):
        count += 1

print("Total Files:", count)