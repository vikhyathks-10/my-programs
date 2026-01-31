# =====================================
# 1️⃣ Combine LOOPS + IF
# Print even and odd numbers from 1 to 10
# =====================================
print("Even and Odd Numbers (1 to 10):")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


# =====================================
# 2️⃣ Combine LIST + FUNCTION
# Find sum and max of list
# =====================================
def list_operations(lst):
    total = 0
    maximum = lst[0]

    for item in lst:
        total += item
        if item > maximum:
            maximum = item

    return total, maximum


numbers = [10, 20, 5, 30, 15]
sum_list, max_list = list_operations(numbers)

print("\nList:", numbers)
print("Sum of list:", sum_list)
print("Maximum element:", max_list)


# =====================================
# 3️⃣ STRING + DICTIONARY PROGRAM
# Count character frequency
# =====================================
text = input("\nEnter a string for character count: ")
char_freq = {}

for ch in text:
    if ch in char_freq:
        char_freq[ch] += 1
    else:
        char_freq[ch] = 1

print("Character Frequency:", char_freq)


# =====================================
# 4️⃣ MINI PROJECT – Menu Driven Calculator
# =====================================
print("\nMini Project: Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid choice")


# =====================================
# 5️⃣ BEST REVISION PROGRAM
# Prime Number Check using Function
# =====================================
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


num = int(input("\nEnter a number to check prime: "))
if is_prime(num):
    print("Prime number")
else:
    print("Not a prime number")
