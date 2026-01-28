# 1️⃣ Armstrong Number
num = int(input("Enter a number to check Armstrong: "))
temp = num
digits = len(str(num))
arm_sum = 0

while temp > 0:
    digit = temp % 10
    arm_sum += digit ** digits
    temp //= 10

if arm_sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


# 2️⃣ Perfect Number
num = int(input("\nEnter a number to check Perfect: "))
sum_div = 0

for i in range(1, num):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("Perfect number")
else:
    print("Not a perfect number")


# 3️⃣ Strong Number
num = int(input("\nEnter a number to check Strong: "))
temp = num
strong_sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    strong_sum += fact
    temp //= 10

if strong_sum == num:
    print("Strong number")
else:
    print("Not a strong number")


# 4️⃣ Fibonacci Series
n = int(input("\nEnter number of Fibonacci terms: "))
a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 5️⃣ GCD of Two Numbers
a = int(input("\nEnter first number for GCD: "))
b = int(input("Enter second number for GCD: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)
