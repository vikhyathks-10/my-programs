# 02_append_file.py

filename = "notes.txt"

with open(filename, "a") as file:
    file.write("Python is powerful.\n")

print("Data appended successfully.")

with open(filename, "r") as file:
    print(file.read())