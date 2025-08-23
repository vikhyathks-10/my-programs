num = int(input("Enter a number: "))
square = num ** 2
if str(square).endswith(str(num)):
    print(num, "is Automorphic")
else:
    print(num, "is not Automorphic")
