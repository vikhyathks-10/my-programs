try:
    user_input = input("Enter a number: ")
    
    if not user_input.isdigit():
        raise ValueError("Input must be a non-negative whole number.")
    
    number = int(user_input)
    digit_sum = 0
    
    while number > 0:
        digit_sum += number % 10
        number //= 10

    print("Sum of digits:", digit_sum)

except ValueError as ve:
    print("Invalid input!", ve)
