num = int(input("Enter a number: "))
digit_sum = sum(int(d) for d in str(num))
if num % digit_sum == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")
