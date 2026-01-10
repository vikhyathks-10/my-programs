# 1️⃣ Print numbers 1 to 10
i = 1
print("Numbers from 1 to 10:")
while i <= 10:
    print(i)
    i += 1


# 2️⃣ Print numbers 10 to 1
i = 10
print("\nNumbers from 10 to 1:")
while i >= 1:
    print(i)
    i -= 1


# 3️⃣ Sum of first 10 numbers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1

print("\nSum of first 10 numbers:", total)


# 4️⃣ Print even numbers (1 to 20)
i = 1
print("\nEven numbers from 1 to 20:")
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


# 5️⃣ Print odd numbers (1 to 20)
i = 1
print("\nOdd numbers from 1 to 20:")
while i <= 20:
    if i % 2 != 0:
        print(i)
    i += 1
