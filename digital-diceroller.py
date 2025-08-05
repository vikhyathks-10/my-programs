import random
while True:
    input("Press Enter to roll the dice...")
    dice_value = random.randint(1, 6)
    print(f"You rolled a {dice_value}")
    
    choice = input("Roll again? (y/n): ")
    if choice.lower() != 'y':
        print("Thank you for playing!")
        break
