# Sum digits until one digit remains

num = 9875
print("Original Number:", num)

while num > 9:
    num = sum(int(digit) for digit in str(num))

print("Single Digit Sum:", num)

