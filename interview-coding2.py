# Write a Python program to Reverse a String
"""
With Indexing:
def reverse_string(s):
    return s[::-1]

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
"""
"""
Without Indexing:
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
"""
#Write a Python program to Check Palindrome
"""
For String:

def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Example usage
input_string = "A man, a plan, a canal, Panama"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
"""
"""
For Number:

def is_palindrome(number):
    # Convert number to string for easy manipulation
    num_str = str(number)
    return num_str == num_str[::-1]

# Example usage
input_number = 12321
if is_palindrome(input_number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
"""
#Write a Python program to Count Vowels in a String
"""
def count_vowels(s):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Initialize count
    count = 0
    # Count vowels
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print("Number of vowels in the string:", vowel_count)
"""
#Write a Python program to find Factorial with Recursion
"""
With Function:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print("Factorial of", number, "is", result)
"""
"""
Without Function:
number = 5
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)
"""
#Write a Python program to find Fibonacci Sequence
"""
def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the sequence with the first two terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence

# Example usage
num_terms = 10
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fib_sequence)"""
#Write a Python program to find Maximum Element in a List
"""
Using Built-in Function:

# Example list
my_list = [10, 23, 45, 67, 12, 89, 34]

# Find maximum element
max_element = max(my_list)

print("Maximum element in the list:", max_element)
Output:

Maximum element in the list: 89
"""
"""
Using User-defined Function:

def find_max_element(lst):
    if not lst:  # If the list is empty
        return None  # Return None since there is no maximum element
    max_element = lst[0]  # Initialize max_element with the first element of the list
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# Example usage
my_list = [10, 23, 45, 67, 12, 89, 34]
max_element = find_max_element(my_list)
print("Maximum element in the list:", max_element)
"""
#Write a Python program to find Anagram Check
"""
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "Listen"
string2 = "Silent"
if are_anagrams(string1, string2):
    print(string1, "and", string2, "are anagrams.")
else:
    print(string1, "and", string2, "are not anagrams.")
"""
#Write a Python program to find Prime Numbers
"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
for num in range(1, 21):
    if is_prime(num):
        print(num, "is a prime number.")"""
#Write a Python program to check for Pangram
"""
import string

def is_pangram(sentence):
    # Convert sentence to lowercase for case-insensitive comparison
    sentence = sentence.lower()
    # Create a set of unique characters in the sentence
    unique_chars = set(sentence)
    # Remove non-alphabetic characters and spaces
    unique_chars.discard(" ")
    unique_chars.difference_update(set(string.punctuation))
    # Check if all letters of the alphabet are present
    return len(unique_chars) == 26

# Example usage
input_sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")"""
#Write a Python program to basic Data Structure Operations (e.g., list manipulation, string manipulation)
"""
# List manipulation
my_list = [1, 2, 3, 4, 5]

# Append an element to the list
my_list.append(6)
print("After appending 6:", my_list)

# Remove an element from the list
my_list.remove(3)
print("After removing 3:", my_list)

# Access elements by index
print("Element at index 2:", my_list[2])

# String manipulation
my_string = "Hello, World!"

# Split the string into a list of words
words = my_string.split()
print("Split string into words:", words)

# Join elements of a list into a single string
new_string = "-".join(words)
print("Joined words with '-':", new_string)

# Convert string to uppercase
upper_string = my_string.upper()
print("Uppercase string:", upper_string)

# Replace a substring
replaced_string = my_string.replace("World", "Universe")
print("After replacing 'World' with 'Universe':", replaced_string)
Output:

After appending 6: [1, 2, 3, 4, 5, 6]
After removing 3: [1, 2, 4, 5, 6]
Element at index 2: 4
Split string into words: ['Hello,', 'World!']
Joined words with '-': Hello,-World!
Uppercase string: HELLO, WORLD!
After replacing 'World' with 'Universe': Hello, Universe!
"""