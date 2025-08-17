arr = [10, 21, 4, 45, 66, 93]

even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)
