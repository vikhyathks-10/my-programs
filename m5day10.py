import re

text = """
Visit https://www.google.com and http://example.org

Learning #Python and #MachineLearning is fun!

Meeting dates:
12-05-2025
01/01/2024

Hello@# Python!! 123
"""

# ---------------------------------------------------
# 1. Extract URLs
# ---------------------------------------------------

urls = re.findall(r'https?://\S+', text)

print("URLs Found:")
for url in urls:
    print(url)

# ---------------------------------------------------
# 2. Extract Hashtags
# ---------------------------------------------------

hashtags = re.findall(r'#\w+', text)

print("\nHashtags Found:")
for tag in hashtags:
    print(tag)

# ---------------------------------------------------
# 3. Find Dates
# ---------------------------------------------------

dates = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', text)

print("\nDates Found:")
for date in dates:
    print(date)

# ---------------------------------------------------
# 4. Replace Spaces with Underscore
# ---------------------------------------------------

replaced_spaces = re.sub(r'\s+', '_', text)

print("\nText After Replacing Spaces:")
print(replaced_spaces)

# ---------------------------------------------------
# 5. Remove Special Characters
# ---------------------------------------------------

clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

print("\nText After Removing Special Characters:")
print(clean_text)