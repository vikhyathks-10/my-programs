# 🔹 DAY 5 - RANDOM MODULE

import random
import string


# 🔹 1. Random Number Generator

print("\n--- Random Number Generator ---")

num = random.randint(1, 100)

print("Random Number:", num)


# 🔹 2. Dice Simulator

print("\n--- Dice Simulator ---")

dice = random.randint(1, 6)

print("Dice Value:", dice)


# 🔹 3. Coin Toss

print("\n--- Coin Toss ---")

coin = random.choice(["Heads", "Tails"])

print("Result:", coin)


# 🔹 4. Random Password Generator

print("\n--- Random Password Generator ---")

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(8):
    password += random.choice(characters)

print("Password:", password)


# 🔹 5. Random OTP Generator

print("\n--- Random OTP Generator ---")

otp = ""

for i in range(6):
    otp += str(random.randint(0, 9))

print("OTP:", otp)