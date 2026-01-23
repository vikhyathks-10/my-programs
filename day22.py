# 1️⃣ Create a Dictionary
student = {
    "name": "Vikyt",
    "age": 19,
    "course": "Computer Science"
}
print("Initial Dictionary:", student)


# 2️⃣ Access Value using Key
print("\nAccessing value:")
print("Name:", student["name"])
print("Age:", student["age"])


# 3️⃣ Add a New Key-Value Pair
student["college"] = "PS College"
print("\nAfter adding new key-value:", student)


# 4️⃣ Update an Existing Value
student["age"] = 20
print("\nAfter updating age:", student)


# 5️⃣ Delete a Key
del student["course"]
print("\nAfter deleting key 'course':", student)
