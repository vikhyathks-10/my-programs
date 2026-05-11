# 🔹 DAY 11 - ADVANCED REGEX PRACTICE

import re
from collections import Counter


# 🔹 1. Validate IP Address

def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    if re.match(pattern, ip):
        parts = ip.split('.')

        for part in parts:
            if int(part) > 255:
                return False

        return True

    return False


# 🔹 2. Validate Vehicle Number (Indian Format)

def validate_vehicle(vehicle):
    pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
    return bool(re.match(pattern, vehicle))


# 🔹 3. Extract Capital Words

def extract_capitals(text):
    pattern = r'\b[A-Z]{2,}\b'
    return re.findall(pattern, text)


# 🔹 4. Word Frequency using Regex

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    freq = Counter(words)

    return freq


# 🔹 5. HTML Tag Extraction

def extract_html_tags(html):
    pattern = r'<.*?>'
    return re.findall(pattern, html)


# 🔹 MAIN PROGRAM

print("\n--- IP Address Validation ---")
print(validate_ip("192.168.1.1"))


print("\n--- Vehicle Number Validation ---")
print(validate_vehicle("KA01AB1234"))


print("\n--- Extract Capital Words ---")
text = "Python is used by NASA and ISRO"
print(extract_capitals(text))


print("\n--- Word Frequency ---")
sentence = "Python is easy and Python is powerful"
print(word_frequency(sentence))


print("\n--- HTML Tag Extraction ---")
html = "<h1>Hello</h1><p>Welcome</p>"
print(extract_html_tags(html))