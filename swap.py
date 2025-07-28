try:
    
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    print("Before swapping:")
    print("a =", a)
    print("b =", b)

    a, b = b, a

    print("After swapping:")
    print("a =", a)
    print("b =", b)

except ValueError:
    print("Invalid input! Please enter numbers only.")
