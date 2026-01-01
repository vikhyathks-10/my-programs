# Write a Python program to check if a string is a palindrome.
"""
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "madam"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
"""
# Write a Python program to find the factorial of a number.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test the function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")"""
# Write a Python program to find the largest element in a list.
"""
def find_largest_element(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Test the function
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest = find_largest_element(numbers)
print(f"The largest element in the list is {largest}")
"""
# Write a Python program to reverse a string.
"""
def reverse_string(s):
    return s[::-1]

# Test the function
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")
"""
#Write a Python program to count the frequency of each element in a list.
""" 
def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)"""
#Write a Python program to check if a number is prime.
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = 29
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")"""
#Write a Python program to find the common elements between two lists.
"""
def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return common_elements

# Test the function
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = find_common_elements(list_a, list_b)
print(f"The common elements are: {common}")
"""
#Write a Python program to sort a list of elements using the bubble sort algorithm.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print(f"The sorted list is: {sorted_list}")
"""
#Write a Python program to find the second largest number in a list.
"""
def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    first = second = float('-inf')
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float('-inf') else None

# Test the function
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
second_largest = find_second_largest(nums)
print(f"The second largest number is: {second_largest}")
"""
#Write a Python program to remove duplicates from a list.
"""
def remove_duplicates(lst):
    return list(set(lst))

# Test the function
numbers = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_numbers = remove_duplicates(numbers)
print(f"The list after removing duplicates is: {unique_numbers}")
"""
#Write a Python program to find the majority element in a list (the element that appears more than n/2 times).
"""
arr=[3,3,4,2,4,4,2,4,4]
count={}
for num in arr:
    count[num]=count.get(num,0)+1
majority_element=None
for key,value in count.items():
    if value>len(arr)//2:
        majority_element=key
        break
print(f"The majority element is: {majority_element}")   """
