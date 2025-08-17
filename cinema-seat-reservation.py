def cinema_seat_reservation():
    seats = [False] * 10  # 10 seats, False = available
    
    while True:
        print("\nSeats status:")
        for i, booked in enumerate(seats, 1):
            status = "Booked" if booked else "Available"
            print(f"Seat {i}: {status}")
        
        choice = input("Enter seat number to book or 'exit' to quit: ")
        if choice.lower() == 'exit':
            print("Exiting seat reservation.")
            break
        if not choice.isdigit():
            print("Invalid input.")
            continue
        seat_num = int(choice)
        if seat_num < 1 or seat_num > len(seats):
            print("Seat number out of range.")
            continue
        if seats[seat_num - 1]:
            print("Sorry, seat already booked.")
        else:
            seats[seat_num - 1] = True
            print(f"Seat {seat_num} successfully booked.")

cinema_seat_reservation()
        