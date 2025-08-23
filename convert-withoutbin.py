# Convert decimal to binary manually
num = 13
print("Decimal:", num)

binary = ""
while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Binary:", binary)
