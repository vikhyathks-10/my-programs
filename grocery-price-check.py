def grocery_price_checker():
    prices = {
        "rice": 50,
        "wheat": 40,
        "sugar": 45,
        "salt": 20,
        "oil": 100
    }
    
    print("Available groceries and prices (Rs/kg):")
    for item, price in prices.items():
        print(f"{item} - Rs {price}")
    
    total = 0
    while True:
        item = input("Enter grocery item to buy (or 'done' to finish): ").lower()
        if item == 'done':
            break
        if item not in prices:
            print("Item not available.")
            continue
        qty = input(f"Enter quantity (kg) of {item}: ")
        if not qty.isdigit() or int(qty) <= 0:
            print("Invalid quantity.")
            continue
        qty = int(qty)
        cost = prices[item] * qty
        total += cost
        print(f"Added {qty} kg of {item} for Rs {cost}.")
    
    print(f"Total price for your grocery list: Rs {total}")

grocery_price_checker()
