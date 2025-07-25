import random

secret = random.randint(1, 100)
attempts = 3

print("Guess the number between 1 and 100")
print("You have only 3 chances!\n")

for i in range(1, attempts + 1):
    guess = int(input(f"Attempt {i}: Enter your guess: "))

    if guess == secret:
        print("Correct! You guessed the number!")
        break
    elif guess < secret:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    if i == attempts:
        print("\nOut of attempts! The correct number was:", secret)
