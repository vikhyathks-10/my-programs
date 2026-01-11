# 1️⃣ Print numbers 1 to 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)


# 2️⃣ Print even numbers (1 to 20)
print("\nEven numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 3️⃣ Print squares of numbers (1 to 10)
print("\nSquares of numbers from 1 to 10:")
for i in range(1, 11):
    print(i, "square =", i * i)


# 4️⃣ Print cubes of numbers (1 to 10)
print("\nCubes of numbers from 1 to 10:")
for i in range(1, 11):
    print(i, "cube =", i * i * i)


# 5️⃣ Multiplication Table
num = int(input("\nEnter a number for multiplication table: "))
print("Multiplication Table of", num)

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
