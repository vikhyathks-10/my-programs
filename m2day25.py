# 1️⃣ Word Frequency Counter
sentence = input("Enter a sentence: ").lower()
words = sentence.split()

word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord Frequency:", word_freq)


# 2️⃣ Character Frequency
text = input("\nEnter a string for character frequency: ")
char_freq = {}

for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print("Character Frequency:", char_freq)


# 3️⃣ Phone Book Dictionary
phone_book = {}
n = int(input("\nEnter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number

print("Phone Book:", phone_book)

search = input("Enter name to search: ")
if search in phone_book:
    print("Phone number:", phone_book[search])
else:
    print("Contact not found")


# 4️⃣ Dictionary from Two Lists
keys = input("\nEnter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()

dict_from_lists = {}

for i in range(min(len(keys), len(values))):
    dict_from_lists[keys[i]] = values[i]

print("Dictionary from two lists:", dict_from_lists)


# 5️⃣ Square of Numbers Dictionary
limit = int(input("\nEnter limit for squares: "))
square_dict = {}

for i in range(1, limit + 1):
    square_dict[i] = i * i

print("Square Dictionary:", square_dict)