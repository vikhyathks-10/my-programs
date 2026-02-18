# =====================================
# 1️⃣ Menu-Driven List Program
# =====================================
numbers = []

while True:
    print("\nMenu:")
    print("1. Add Element")
    print("2. Display List")
    print("3. Remove Element")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter element to add: "))
        numbers.append(val)

    elif choice == 2:
        print("List:", numbers)

    elif choice == 3:
        val = int(input("Enter element to remove: "))
        if val in numbers:
            numbers.remove(val)
        else:
            print("Element not found")

    elif choice == 4:
        break

    else:
        print("Invalid choice")


# =====================================
# 2️⃣ Student Marks List Analysis
# =====================================
n = int(input("\nEnter number of students: "))
marks = []

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

print("Marks:", marks)
print("Total:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))


# =====================================
# 3️⃣ Find Pair with Given Sum
# =====================================
target = int(input("\nEnter target sum: "))
found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print("Pair found:", numbers[i], numbers[j])
            found = True

if not found:
    print("No pair found")


# =====================================
# 4️⃣ List of Prime Numbers (1 to n)
# =====================================
limit = int(input("\nEnter limit for prime numbers: "))
primes = []

for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("Prime numbers:", primes)


# =====================================
# 5️⃣ List Comprehension Practice
# =====================================
squares = [x*x for x in range(1, 11)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print("Squares (1–10):", squares)
print("Even numbers (1–20):", even_numbers)
