# 04_json_file.py

import json

student = {
    "name": "Rahul",
    "age": 20,
    "branch": "CSE",
    "marks": 92
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON Saved Successfully.\n")

with open("student.json", "r") as file:
    data = json.load(file)

print(data)