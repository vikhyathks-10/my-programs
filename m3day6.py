import os

file_name = "sample.txt"

# =====================================
# 1️⃣ Check if File Exists
# =====================================
if os.path.exists(file_name):
    print("File exists")
else:
    print("File does not exist")


# =====================================
# 2️⃣ Reverse File Content
# =====================================
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        content = file.read()

    reversed_content = content[::-1]

    with open("reversed.txt", "w") as file:
        file.write(reversed_content)

    print("Reversed content saved to reversed.txt")


# =====================================
# 3️⃣ Sort Lines Alphabetically
# =====================================
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    lines.sort()

    with open("sorted.txt", "w") as file:
        file.writelines(lines)

    print("Sorted lines saved to sorted.txt")


# =====================================
# 4️⃣ Remove Duplicate Lines
# =====================================
if os.path.exists(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    unique_lines = list(set(lines))

    with open("unique.txt", "w") as file:
        file.writelines(unique_lines)

    print("Duplicate lines removed and saved to unique.txt")


# =====================================
# 5️⃣ Rename a File
# =====================================
new_name = "renamed_sample.txt"

if os.path.exists(file_name):
    os.rename(file_name, new_name)
    print("File renamed to", new_name)
else:
    print("File not found to rename")