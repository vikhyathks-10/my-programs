# 🔹 DAY 14 - MIXED REGEX PRACTICE

import re


# 🔹 Q1. Extract Hashtags from Text

def extract_hashtags(text):

    pattern = r'#\w+'

    return re.findall(pattern, text)


# 🔹 Q2. Find Dates in Format DD-MM-YYYY

def find_dates(text):

    pattern = r'\b\d{2}-\d{2}-\d{4}\b'

    return re.findall(pattern, text)


# 🔹 Q3. Remove Extra Spaces

def remove_extra_spaces(text):

    return re.sub(r'\s+', ' ', text).strip()


# 🔹 Q4. Extract URLs

def extract_urls(text):

    pattern = r'https?://[^\s]+'

    return re.findall(pattern, text)


# 🔹 Q5. Validate Hex Color Code

def validate_hex(color):

    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'

    return bool(re.match(pattern, color))


# 🔹 MAIN PROGRAM

print("\n--- Extract Hashtags ---")

text1 = "Learning #Python and #Regex is fun"

print(extract_hashtags(text1))


print("\n--- Find Dates ---")

text2 = "Exam dates are 15-08-2025 and 01-01-2026"

print(find_dates(text2))


print("\n--- Remove Extra Spaces ---")

text3 = "Python     is     very     powerful"

print(remove_extra_spaces(text3))


print("\n--- Extract URLs ---")

text4 = """
Visit https://google.com
and http://example.com
"""

print(extract_urls(text4))


print("\n--- Validate Hex Color ---")

print(validate_hex("#FF5733"))
print(validate_hex("#abc"))
print(validate_hex("123456"))