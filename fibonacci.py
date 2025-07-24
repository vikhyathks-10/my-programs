def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_sum(n):
    sum = 0
    print("Fibonacci Series:")
    for i in range(n):
        num = fib(i)
        print(num)
        sum += num
    print()
    return sum

try:
    n = int(input("Enter how many Fibonacci numbers you want: "))
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        total = fib_sum(n)
        print("Sum of first", n, "Fibonacci numbers is:", total)
except:
    print("Invalid input. Please enter an integer.")
