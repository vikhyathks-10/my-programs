"""coding interview problems - solutions in Python
Sum of all even numbers in a list
nums = [1,2,3,4,5,6]
even_sum = sum(x for x in nums if x % 2 == 0)
print(even_sum)  # 12

Sum of all odd numbers in a list
nums = [1,2,3,4,5,6]
odd_sum = sum(x for x in nums if x % 2 != 0)
print(odd_sum)  # 9

Remove all punctuation from a string
import string
s = "Hello, world! How's it going?"
clean = ''.join(ch for ch in s if ch not in string.punctuation)
print(clean)

Find common elements between two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]
common = list(set(list1) & set(list2))
print(common)  # [3, 4]

Merge two sorted lists into one sorted list
a = [1,3,5]
b = [2,4,6]
merged = sorted(a + b)
print(merged)  # [1,2,3,4,5,6]

Find the most frequent element in a list
from collections import Counter
nums = [1,2,2,3,3,3,4]
freq = Counter(nums)
most_common = freq.most_common(1)[0][0]
print(most_common)  # 3

Sort a dictionary by its values
d = {'a':3, 'b':1, 'c':2}
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_value)

Sort a dictionary by its keys
d = {'b':2, 'a':3, 'c':1}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)

Swap two numbers without a third variable
a, b = 5, 10
a = a + b
b = a - b
a = a - b
print(a, b)  # 10 5

Count uppercase and lowercase letters in a string
s = "Hello World"
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print(upper, lower)  # 2 8
"""