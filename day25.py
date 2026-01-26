# 1️⃣ Max of Two Numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Maximum number:", max_of_two(x, y))


# 2️⃣ String Reverse Function
def reverse_string(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    return rev

s = input("\nEnter a string: ")
print("Reversed string:", reverse_string(s))


# 3️⃣ Count Vowels Function
def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

print("Number of vowels:", count_vowels(s))


# 4️⃣ Sum of List Function
def sum_of_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

n = int(input("\nHow many elements in list: "))
numbers = []

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    numbers.append(val)

print("Sum of list elements:", sum_of_list(numbers))


# 5️⃣ Area of Circle Function
def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius

r = float(input("\nEnter radius of circle: "))
print("Area of circle:", area_of_circle(r))
