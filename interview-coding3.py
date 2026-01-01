# Write a Python program to find Minimum Element in a List?
"""
Using User-defined:

def find_min_element(lst):
    if not lst:  # If the list is empty
        return None  # Return None since there is no minimum element
    min_element = lst[0]  # Initialize min_element with the first element of the list
    for num in lst:
        if num < min_element:
            min_element = num
    return min_element

# Example usage
my_list = [10, 23, 45, 67, 12, 89, 34]
min_element = find_min_element(my_list)
print("Minimum element in the list:", min_element)
Output:

Minimum element in the list: 10"""
"""
Using Built-in Function:

my_list = [10, 23, 45, 67, 12, 89, 34]
min_element = min(my_list)
print("Minimum element in the list:", min_element)
Output:

Minimum element in the list: 10"""
#Write a Python program to calculate Sum of Digits in a Number
"""
def sum_of_digits(number):
    # Convert number to string to iterate through its digits
    num_str = str(number)
    # Initialize sum
    digit_sum = 0
    # Iterate through each digit and add it to the sum
    for digit in num_str:
        digit_sum += int(digit)
    return digit_sum

# Example usage
input_number = 12345
result = sum_of_digits(input_number)
print("Sum of digits in", input_number, "is", result)
Output:

Sum of digits in 12345 is 15"""

#Write a Python program to check for Armstrong Number
"""
def is_armstrong(number):
    # Convert number to string to get its length
    num_str = str(number)
    # Get the number of digits
    num_digits = len(num_str)
    # Initialize sum
    armstrong_sum = 0
    # Calculate the sum of digits raised to the power of the number of digits
    for digit in num_str:
        armstrong_sum += int(digit) ** num_digits
    # Check if the sum is equal to the original number
    return armstrong_sum == number

# Example usage
input_number = 153
if is_armstrong(input_number):
    print(input_number, "is an Armstrong number.")
else:
    print(input_number, "is not an Armstrong number.")
Output:

153 is an Armstrong number."""
# Write a Python program to check for Leap Year?
"""
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
input_year = 2024
if is_leap_year(input_year):
    print(input_year, "is a leap year.")
else:
    print(input_year, "is not a leap year.")
Output:

2024 is a leap year. """

# Write a Python program to calculate Factorial without Recursion?
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
result = factorial(number)
print("Factorial of", number, "is", result)
Output:

Factorial of 5 is 120"""
# Write a Python program to find Average of Numbers in a List?
"""
def find_average(numbers):
    if not numbers:  # If the list is empty
        return None  # Return None since there are no numbers to average
    total = sum(numbers)  # Calculate the sum of numbers in the list
    average = total / len(numbers)  # Calculate the average
    return average

# Example usage
number_list = [10, 20, 30, 40, 50]
average = find_average(number_list)
if average is not None:
    print("Average of numbers in the list:", average)
else:
    print("The list is empty.")
Output:

Average of numbers in the list: 30.0""" 
#  Write a Python program to Merge Two Sorted Lists?
"""
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Append remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
merged_list = merge_sorted_lists(list1, list2)
print("Merged sorted list:", merged_list)
Output:

Merged sorted list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""
#Write a Python program to Remove Duplicates from a String?
"""
def remove_duplicates(input_string):
    # Initialize an empty set to store unique characters
    unique_chars = set()
    # Initialize an empty string to store the result
    result = ""
    # Iterate through each character in the input string
    for char in input_string:
        # Add the character to the result string if it's not already in the set
        if char not in unique_chars:
            result += char
            unique_chars.add(char)
    return result

# Example usage
input_string = "hello world"
result = remove_duplicates(input_string)
print("String with duplicates removed:", result)
Output:

String with duplicates removed: helo wrd"""
#Write a Python program to Check for Perfect Number?
"""
def is_perfect_number(number):
    if number <= 0:
        return False
    divisor_sum = 0
    # Find proper divisors and sum them up
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    # Check if the sum of proper divisors equals the number
    return divisor_sum == number

# Example usage
input_number = 28
if is_perfect_number(input_number):
    print(input_number, "is a perfect number.")
else:
    print(input_number, "is not a perfect number.")
Output:

28 is a perfect number."""
# Write a Python program to Find Maximum Difference between Two Elements in a List?
"""
def max_difference(nums):
    if len(nums) < 2:
        return None  # If the list has less than two elements, return None
    min_element = float('inf')  # Initialize min_element to positive infinity
    max_difference = float('-inf')  # Initialize max_difference to negative infinity
    for num in nums:
        min_element = min(min_element, num)
        max_difference = max(max_difference, num - min_element)
    return max_difference

# Example usage
numbers = [7, 1, 5, 3, 6, 4]
result = max_difference(numbers)
if result is not None:
    print("Maximum difference between two elements in the list:", result)
else:
    print("The list has less than two elements.")
Output:

Maximum difference between two elements in the list: 5"""