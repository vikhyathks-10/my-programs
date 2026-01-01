#Write a Python program to check if a Number is Even or Odd
"""
With User-defined Function:

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
input_number = 7
result = check_even_odd(input_number)
print(input_number, "is", result)
Output:

7 is Odd"""
"""
Without Function:

number = 7

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")
Output:

7 is Odd"""

#Write a Python program to Count Words in a Sentence?
"""
def count_words(sentence):
    # Split the sentence into words using whitespace as the delimiter
    words = sentence.split()
    # Count the number of words
    return len(words)

# Example usage
input_sentence = "This is a sample sentence."
word_count = count_words(input_sentence)
print("Number of words in the sentence:", word_count)
Output:

Number of words in the sentence: 5"""
"""
With Built-in Fucntion:

sentence = "This is a sample sentence."
word_count = len(sentence.split())
print("Number of words in the sentence:", word_count)
Output:

Number of words in the sentence: 5"""
"""
Without Built-in Function:

sentence = "This is a sample sentence."
word_count = 0
# Flag to indicate if the current character is part of a word
in_word = False
# Iterate through each character in the sentence
for char in sentence:
    # If the character is not a space and we are not already in a word
    if char != ' ' and not in_word:
        # Increment word count and set the flag to indicate we are in a word
        word_count += 1
        in_word = True
    # If the character is a space and we are in a word
    elif char == ' ' and in_word:
        # Set the flag to indicate we are not in a word
        in_word = False

print("Number of words in the sentence:", word_count)
Output:

Number of words in the sentence: 5"""
#Write a Python program to Convert Decimal to Binary?
"""
def decimal_to_binary(decimal):
    binary = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        binary = str(remainder) + binary
        quotient //= 2
    return binary

# Example usage
decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is", binary_number)
Output:

Binary representation of 10 is 1010"""
#Write a Python program to Find Second Largest Element in a List?
"""
def second_largest(nums):
    if len(nums) < 2:
        return None  # If the list has less than two elements, return None
    sorted_nums = sorted(nums, reverse=True)  # Sort the list in descending order
    return sorted_nums[1]  # Return the second element (index 1)

# Example usage
numbers = [10, 30, 20, 40, 50]
result = second_largest(numbers)
if result is not None:
    print("Second largest element in the list:", result)
else:
    print("The list has less than two elements.")
Output:

Second largest element in the list: 40"""
#Write a Python program to Reverse Words in a String?
"""
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse the order of words
    reversed_words = words[::-1]
    # Join the reversed words back into a string
    reversed_string = " ".join(reversed_words)
    return reversed_string

# Example usage
input_string = "Hello World"
reversed_string = reverse_words(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
Output:

Original string: Hello World 
Reversed string: World Hello"""
# Write a Python program to check if a Number is a Prime Factor?
"""
def is_prime_factor(number, potential_factor):
    if number <= 1 or potential_factor <= 1:
        return False  # Numbers less than or equal to 1 are not considered prime factors
    return number % potential_factor == 0

# Example usage
number = 15
potential_factor = 3
if is_prime_factor(number, potential_factor):
    print(potential_factor, "is a prime factor of", number)
else:
    print(potential_factor, "is not a prime factor of", number)
Output:

3 is a prime factor of 15"""
#Write a Python program to check if a Number is a Power of Two?
"""
def is_power_of_two(number):
    if number <= 0:
        return False  # Numbers less than or equal to 0 are not powers of two
    while number > 1:
        if number % 2 != 0:
            return False  # If the number is not divisible by 2, it's not a power of two
        number //= 2
    return True

# Example usage
number = 16
if is_power_of_two(number):
    print(number, "is a power of two.")
else:
    print(number, "is not a power of two.")
Output:

16 is a power of two."""
# Write a Python program to convert Celsius to Fahrenheit?
"""
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius_temperature = 25
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print("Celsius:", celsius_temperature, "Fahrenheit:", fahrenheit_temperature)
Output:

Celsius: 25 Fahrenheit: 77.0"""
# Write a Python program to calculate LCM (Least Common Multiple) of Two Numbers?
"""
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage
num1 = 12
num2 = 18
result = lcm(num1, num2)
print("LCM of", num1, "and", num2, "is", result)
Output:

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Example usage
num1 = 12
num2 = 18
result = lcm(num1, num2)
print("LCM of", num1, "and", num2, "is", result)
Output:

LCM of 12 and 18 is 36"""