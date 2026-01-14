# 1️⃣ Print stars in one line
print("Stars in one line:")
for i in range(5):
    print("*", end=" ")
print("\n")


# 2️⃣ Right triangle star pattern
print("Right Triangle Stars:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


# 3️⃣ Number triangle
print("\nNumber Triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# 4️⃣ Repeated number pattern
print("\nRepeated Number Pattern:")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()


# 5️⃣ Alphabet pattern
print("\nAlphabet Pattern:")
ch = ord('A')
for i in range(1, 6):
    for j in range(i):
        print(chr(ch), end=" ")
    ch += 1
    print()
