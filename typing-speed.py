import time
import random

paragraphs = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language used for web development, data science, and more.",
    "Typing quickly and accurately is a valuable skill in today's digital world.",
    "Consistent practice helps improve typing speed and reduces errors.",
    "Artificial Intelligence is changing how we interact with technology every day."
]

test_text = random.choice(paragraphs)

print("\n--- Typing Speed Test ---")
print("\nType the following paragraph:\n")
print(test_text)
input("\nPress Enter when you're ready to start typing...")

start_time = time.time()
typed_text = input("\nStart typing below:\n")
end_time = time.time()

time_taken = end_time - start_time 
time_taken_minutes = time_taken / 60

typed_words = typed_text.split()
word_count = len(typed_words)
wpm = word_count / time_taken_minutes
original_words = test_text.split()
correct_words = 0

for orig, typed in zip(original_words, typed_words):
    if orig == typed:
        correct_words += 1

accuracy = (correct_words / len(original_words)) * 100
print("\n--- Results ---")
print(f"🕒 Time taken: {round(time_taken, 2)} seconds")
print(f"💨 Words per minute (WPM): {int(wpm)}")
print(f"🎯 Accuracy: {round(accuracy, 2)}%")
print("\nThank you for participating in the typing speed test!")