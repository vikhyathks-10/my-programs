def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a Prime Number.")
    else:
        print(number, "is NOT a Prime Number.")
except:
    print("Invalid input! Please enter a valid integer.")
