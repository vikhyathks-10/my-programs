def is_even(n):
    return n % 2 == 0

num = int(input("Enter a number: "))
print("Even" if is_even(num) else "Odd")
print(num, "is Even" if is_even(num) else "is Odd")