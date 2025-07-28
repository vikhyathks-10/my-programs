num = int(input("Enter a number: "))
temp = num
n = len(str(num))  # Count the number of digits
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
