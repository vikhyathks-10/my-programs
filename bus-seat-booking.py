def bus_seat_booking():
    seats = [False]*10  # 10 seats, False means available
    while True:
        print("\nSeats (number: status):")
        for i, booked in enumerate(seats, 1):
            status = "Booked" if booked else "Available"
            print(f"{i}: {status}")
        choice = input("Enter seat number to book or 'exit' to quit: ")
        if choice.lower() == 'exit':
            break
        if not choice.isdigit():
            print("Invalid input.")
            continue
        seat_num = int(choice)
        if seat_num < 1 or seat_num > len(seats):
            print("Seat number out of range.")
            continue
        if seats[seat_num-1]:
            print("Seat already booked.")
        else:
            seats[seat_num-1] = True
            print(f"Seat {seat_num} booked successfully.")

bus_seat_booking()