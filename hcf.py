def calculate_hcf():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    if not (num1.isdigit() and num2.isdigit()):
        print("Please enter valid positive integers.")
        return
    num1, num2 = int(num1), int(num2)

    minimum = min(num1, num2)
    hcf = 1
    for i in range(1, minimum + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    print(f"HCF of {num1} and {num2} is {hcf}")

calculate_hcf()
