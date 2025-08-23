n = int(input("Enter a number: "))
factors = []
i = 2
while i <= n:
    if n % i == 0:
        factors.append(i)
        n //= i
    else:
        i += 1
print("Prime factors:", factors)
