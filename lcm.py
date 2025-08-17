def calculate_lcm():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if not (num1.isdigit() and num2.isdigit()):
        print("Please enter valid positive integers.")
        return
    num1, num2 = int(num1), int(num2)

    start = max(num1, num2)
    while True:
        if start % num1 == 0 and start % num2 == 0:
            print(f"LCM of {num1} and {num2} is {start}")
            break
        start += 1

calculate_lcm()
