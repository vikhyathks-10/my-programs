# 🔹 DAY 12 - REGEX MINI APPLICATIONS

import re


# 🔹 1. Regex Login Validator

def login_validator(username, password):

    user_pattern = r'^[a-zA-Z0-9_]{4,15}$'

    pass_pattern = (
        r'^(?=.*[A-Z])'
        r'(?=.*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[@$!%*?&])'
        r'.{8,}$'
    )

    user_valid = bool(re.match(user_pattern, username))
    pass_valid = bool(re.match(pass_pattern, password))

    return user_valid and pass_valid


# 🔹 2. Chat Filter (Bad Word Detector)

def bad_word_filter(text):

    bad_words = ["bad", "stupid", "idiot"]

    for word in bad_words:
        pattern = rf'\b{word}\b'
        text = re.sub(pattern, "***", text, flags=re.IGNORECASE)

    return text


# 🔹 3. Text Cleaner

def clean_text(text):

    # remove special characters
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # remove extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned)

    return cleaned.strip()


# 🔹 4. Sentence Splitter

def split_sentences(text):

    sentences = re.split(r'[.!?]+', text)

    return [s.strip() for s in sentences if s.strip()]


# 🔹 5. Data Extractor

def extract_data(text):

    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        text
    )

    phones = re.findall(r'\b[6-9]\d{9}\b', text)

    return {
        "Emails": emails,
        "Phone Numbers": phones
    }


# 🔹 MAIN PROGRAM

print("\n--- Login Validator ---")
print(login_validator("vikyat_123", "Strong@123"))


print("\n--- Chat Filter ---")
msg = "You are stupid and bad"
print(bad_word_filter(msg))


print("\n--- Text Cleaner ---")
dirty = "Hello!!!   Python@@@ is ###awesome..."
print(clean_text(dirty))


print("\n--- Sentence Splitter ---")
para = "Python is easy. Regex is powerful! Do you agree?"
print(split_sentences(para))


print("\n--- Data Extractor ---")
sample = """
Contact us at test@gmail.com
or call 9876543210
"""

print(extract_data(sample))