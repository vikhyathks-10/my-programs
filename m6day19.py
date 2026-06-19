# 🔹 DAY 19 - FILE BASED MINI DATABASE

import csv
import os


class MiniDatabase:

    FILE_NAME = "database.csv"

    # =====================================
    # 🔹 Load Records
    # =====================================

    def load_records(self):

        records = []

        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME, "r", newline="") as file:

                reader = csv.reader(file)

                records = list(reader)

        return records

    # =====================================
    # 🔹 Save Records
    # =====================================

    def save_records(self, records):

        with open(self.FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(records)

    # =====================================
    # 🔹 Insert Record
    # =====================================

    def insert_record(self):

        record_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        records = self.load_records()

        records.append([record_id, name, age])

        self.save_records(records)

        print("✅ Record Inserted Successfully")

    # =====================================
    # 🔹 Search Record
    # =====================================

    def search_record(self):

        search_id = input("Enter ID To Search: ")

        records = self.load_records()

        found = False

        for record in records:

            if record[0] == search_id:

                print("\nRecord Found")

                print(
                    f"ID: {record[0]}, "
                    f"Name: {record[1]}, "
                    f"Age: {record[2]}"
                )

                found = True

                break

        if not found:

            print("❌ Record Not Found")

    # =====================================
    # 🔹 Update Record
    # =====================================

    def update_record(self):

        update_id = input("Enter ID To Update: ")

        records = self.load_records()

        found = False

        for record in records:

            if record[0] == update_id:

                record[1] = input(
                    "Enter New Name: "
                )

                record[2] = input(
                    "Enter New Age: "
                )

                found = True

                break

        if found:

            self.save_records(records)

            print("✅ Record Updated")

        else:

            print("❌ Record Not Found")

    # =====================================
    # 🔹 Delete Record
    # =====================================

    def delete_record(self):

        delete_id = input(
            "Enter ID To Delete: "
        )

        records = self.load_records()

        new_records = []

        found = False

        for record in records:

            if record[0] != delete_id:

                new_records.append(record)

            else:

                found = True

        if found:

            self.save_records(new_records)

            print("✅ Record Deleted")

        else:

            print("❌ Record Not Found")

    # =====================================
    # 🔹 Display All Records
    # =====================================

    def display_records(self):

        records = self.load_records()

        if not records:

            print("No Records Found")
            return

        print("\n===== ALL RECORDS =====")

        for record in records:

            print(
                f"ID: {record[0]} | "
                f"Name: {record[1]} | "
                f"Age: {record[2]}"
            )


# =====================================
# 🔹 MAIN PROGRAM
# =====================================

db = MiniDatabase()

while True:

    print("\n===== MINI DATABASE =====")

    print("1. Insert Record")
    print("2. Search Record")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Display All Records")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        db.insert_record()

    elif choice == "2":

        db.search_record()

    elif choice == "3":

        db.update_record()

    elif choice == "4":

        db.delete_record()

    elif choice == "5":

        db.display_records()

    elif choice == "6":

        print("Goodbye 👋")

        break

    else:

        print("❌ Invalid Choice")