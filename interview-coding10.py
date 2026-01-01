"""interview Coding Questions in Python
Find the longest word in a sentence
sentence = "Python programming is fun"
longest = max(sentence.split(), key=len)
print(longest)  # programming

Find the shortest word in a sentence
sentence = "Python programming is fun"
shortest = min(sentence.split(), key=len)
print(shortest)  # is

Convert a decimal number to binary
num = 10
print(bin(num)[2:])  # 1010

Convert a binary number to decimal
b = "1010"
print(int(b, 2))  # 10

Print multiplication table of a number
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

Check Armstrong number
n = 153
sum_of_digits = sum(int(d)**3 for d in str(n))
print(sum_of_digits == n)  # True

Print all prime numbers in a given range
for num in range(2, 21):
    if all(num%i != 0 for i in range(2,int(num**0.5)+1)):
        print(num, end=" ")

Print all palindromic substrings of a string
s = "aba"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1]:
            print(sub)

Find factorial using reduce() function
from functools import reduce
n = 5
fact = reduce(lambda x,y: x*y, range(1, n+1))
print(fact)  # 120

Check whether a string contains only digits
s = "12345"
print(s.isdigit())  # True
"""