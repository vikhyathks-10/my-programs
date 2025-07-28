try:
    expression = input("Enter your expression: ")
    result = eval(expression)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid expression.")