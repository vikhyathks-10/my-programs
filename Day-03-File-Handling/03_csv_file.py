# 03_csv_file.py

import csv

filename = "students.csv"

data = [
    ["ID", "Name", "Marks"],
    [101, "Rahul", 90],
    [102, "Priya", 85],
    [103, "Amit", 95]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV File Created Successfully.\n")

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)