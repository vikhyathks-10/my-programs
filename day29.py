# 1️⃣ Decimal to Binary
num = int(input("Enter a decimal number: "))
temp = num
binary = ""

if temp == 0:
    binary = "0"
else:
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2

print("Binary:", binary)


# 2️⃣ Binary to Decimal
binary = input("\nEnter a binary number: ")
decimal = 0
power = 0

for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal:", decimal)


# 3️⃣ Decimal to Octal
num = int(input("\nEnter a decimal number: "))
temp = num
octal = ""

if temp == 0:
    octal = "0"
else:
    while temp > 0:
        octal = str(temp % 8) + octal
        temp //= 8

print("Octal:", octal)


# 4️⃣ Decimal to Hexadecimal
num = int(input("\nEnter a decimal number: "))
temp = num
hex_digits = "0123456789ABCDEF"
hexa = ""

if temp == 0:
    hexa = "0"
else:
    while temp > 0:
        hexa = hex_digits[temp % 16] + hexa
        temp //= 16

print("Hexadecimal:", hexa)


# 5️⃣ Count Set Bits (1s in binary)
num = int(input("\nEnter a number to count set bits: "))
count = 0

while num > 0:
    if num % 2 == 1:
        count += 1
    num //= 2

print("Number of set bits:", count)
