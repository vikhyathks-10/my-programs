# 01_text_file.py

filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("Learning File Operations.\n")

print("Data written successfully.\n")

with open(filename, "r") as file:
    print("File Content:")
    print(file.read())