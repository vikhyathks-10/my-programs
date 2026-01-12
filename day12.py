# 1️⃣ Prime Number Check
num = int(input("Enter a number to check prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")


# 2️⃣ Print First 10 Prime Numbers
print("\nFirst 10 Prime Numbers:")
count = 0
n = 2

while count < 10:
    prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n)
        count += 1

    n += 1


# 3️⃣ Sum of Even Numbers (1 to 50)
even_sum = 0
for i in range(1, 51):
    if i % 2 == 0:
        even_sum += i

print("\nSum of even numbers from 1 to 50:", even_sum)


# 4️⃣ Sum of Odd Numbers (1 to 50)
odd_sum = 0
for i in range(1, 51):
    if i % 2 != 0:
        odd_sum += i

print("Sum of odd numbers from 1 to 50:", odd_sum)


# 5️⃣ Count Vowels in a String
text = input("\nEnter a string: ").lower()
vowel_count = 0

for ch in text:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1

print("Number of vowels:", vowel_count)
