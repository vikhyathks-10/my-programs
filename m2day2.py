# 6️⃣ Function to calculate area of rectangle
def area_rectangle(length, width):
    return length * width

print("Area of rectangle:", area_rectangle(10, 5))


# 7️⃣ Function to calculate perimeter of square
def perimeter_square(side):
    return 4 * side

print("Perimeter of square:", perimeter_square(6))


# 8️⃣ Function to find maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum:", max_of_two(12, 9))


# 9️⃣ Function to print numbers from 1 to n
def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

print_numbers(5)


# 🔟 Function to print multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

multiplication_table(4)
