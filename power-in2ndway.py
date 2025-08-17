def calculate_power():
    base = input("Enter base: ")
    exponent = input("Enter exponent (non-negative): ")

    if not (base.lstrip('-').isdigit() and exponent.isdigit()):
        print("Invalid input. Please enter integers.")
        return

    base = int(base)
    exponent = int(exponent)

    result = 1
    for _ in range(exponent):
        result *= base

    print(f"{base}^{exponent} = {result}")

calculate_power()
