def hotel_room_booking():
    available_rooms = 5
    print(f"Welcome! Available rooms: {available_rooms}")
    
    while True:
        if available_rooms == 0:
            print("Sorry, hotel is fully booked.")
            break
        choice = input("Type 'book' to book a room or 'exit' to quit: ").lower()
        if choice == 'book':
            available_rooms -= 1
            print(f"Room booked! Rooms left: {available_rooms}")
        elif choice == 'exit':
            print("Thank you for visiting.")
            break
        else:
            print("Invalid input.")

hotel_room_booking()
