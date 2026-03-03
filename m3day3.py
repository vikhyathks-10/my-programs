# =====================================
# 1️⃣ Create a Text File and Write Data
# =====================================
file_name = "sample.txt"

with open(file_name, "w") as file:
    data = input("Enter data to write into file: ")
    file.write(data + "\n")

print("Data written successfully.")


# =====================================
# 2️⃣ Append Data to Existing File
# =====================================
with open(file_name, "a") as file:
    more_data = input("Enter data to append: ")
    file.write(more_data + "\n")

print("Data appended successfully.")


# =====================================
# 3️⃣ Read Entire File Content
# =====================================
with open(file_name, "r") as file:
    content = file.read()

print("\nFull File Content:")
print(content)


# =====================================
# 4️⃣ Read File Line by Line
# =====================================
print("Reading file line by line:")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())


# =====================================
# 5️⃣ Count Number of Lines
# =====================================
line_count = 0
with open(file_name, "r") as file:
    for line in file:
        line_count += 1

print("Total number of lines:", line_count)