# 🔹 DAY 29 - HOTEL RESERVATION SYSTEM

import csv
import os


class HotelReservation:

    FILE_NAME = "reservations.csv"

    # ==========================================
    # Load Reservations
    # ==========================================

    def load_data(self):

        reservations = []

        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME,
                      "r",
                      newline="") as file:

                reader = csv.reader(file)

                reservations = list(reader)

        return reservations

    # ==========================================
    # Save Reservations
    # ==========================================

    def save_data(self, reservations):

        with open(self.FILE_NAME,
                  "w",
                  newline="") as file:

            writer = csv.writer(file)

            writer.writerows(reservations)

    # ==========================================
    # Book Room
    # ==========================================

    def book_room(self):

        reservations = self.load_data()

        room = input("Enter Room Number : ")

        for reservation in reservations:

            if reservation[0] == room:

                print("❌ Room Already Booked")

                return

        name = input("Enter Customer Name : ")

        days = input("Enter Number of Days : ")

        reservations.append([room, name, days])

        self.save_data(reservations)

        print("✅ Room Booked Successfully")

    # ==========================================
    # View Reservations
    # ==========================================

    def view_reservations(self):

        reservations = self.load_data()

        if not reservations:

            print("No Reservations Found")

            return

        print("\n===== RESERVATIONS =====")

        for reservation in reservations:

            print(
                f"Room : {reservation[0]} | "
                f"Customer : {reservation[1]} | "
                f"Days : {reservation[2]}"
            )

    # ==========================================
    # Search Reservation
    # ==========================================

    def search_reservation(self):

        room = input("Enter Room Number : ")

        reservations = self.load_data()

        for reservation in reservations:

            if reservation[0] == room:

                print("\nReservation Found")

                print("Room :", reservation[0])

                print("Customer :", reservation[1])

                print("Days :", reservation[2])

                return

        print("❌ Reservation Not Found")

    # ==========================================
    # Cancel Reservation
    # ==========================================

    def cancel_reservation(self):

        room = input("Enter Room Number : ")

        reservations = self.load_data()

        updated = []

        found = False

        for reservation in reservations:

            if reservation[0] != room:

                updated.append(reservation)

            else:

                found = True

        if found:

            self.save_data(updated)

            print("✅ Reservation Cancelled")

        else:

            print("❌ Reservation Not Found")

    # ==========================================
    # Generate Bill
    # ==========================================

    def generate_bill(self):

        room = input("Enter Room Number : ")

        reservations = self.load_data()

        price_per_day = 2000

        for reservation in reservations:

            if reservation[0] == room:

                days = int(reservation[2])

                total = days * price_per_day

                print("\n===== BILL =====")

                print("Customer :", reservation[1])

                print("Room :", reservation[0])

                print("Days Stayed :", days)

                print("Price Per Day : ₹", price_per_day)

                print("Total Bill : ₹", total)

                return

        print("❌ Reservation Not Found")


# ==========================================
# Main Program
# ==========================================

hotel = HotelReservation()

while True:

    print("\n========== HOTEL RESERVATION SYSTEM ==========")

    print("1. Book Room")

    print("2. View Reservations")

    print("3. Search Reservation")

    print("4. Cancel Reservation")

    print("5. Generate Bill")

    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        hotel.book_room()

    elif choice == "2":

        hotel.view_reservations()

    elif choice == "3":

        hotel.search_reservation()

    elif choice == "4":

        hotel.cancel_reservation()

    elif choice == "5":

        hotel.generate_bill()

    elif choice == "6":

        print("\nThank You For Visiting 👋")

        break

    else:

        print("\n❌ Invalid Choice")