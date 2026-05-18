# ==========================================
# Daily Utility Toolkit
# ==========================================

import os
import time
import datetime
import pyperclip

# ------------------------------------------
# Notes Saver
# ------------------------------------------

def notes_saver():
    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:
        file.write(note + "\n")

    print("✅ Note saved successfully!\n")


# ------------------------------------------
# Auto Shutdown Timer
# ------------------------------------------

def shutdown_timer():
    minutes = int(input("Enter shutdown time in minutes: "))

    seconds = minutes * 60

    print(f"⚠️ System will shut down in {minutes} minute(s).")

    # Windows shutdown command
    os.system(f"shutdown /s /t {seconds}")


# ------------------------------------------
# Cancel Shutdown
# ------------------------------------------

def cancel_shutdown():
    os.system("shutdown /a")
    print("✅ Shutdown cancelled.\n")


# ------------------------------------------
# Alarm Clock
# ------------------------------------------

def alarm_clock():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")

    print("⏰ Alarm is set...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print(current_time, end="\r")

        if current_time == alarm_time:
            print("\n🔔 WAKE UP! ALARM RINGING!")
            break

        time.sleep(1)


# ------------------------------------------
# Reminder App
# ------------------------------------------

def reminder_app():
    reminder = input("Enter reminder message: ")
    seconds = int(input("Remind after how many seconds? "))

    print("⏳ Reminder set...")

    time.sleep(seconds)

    print(f"\n🔔 REMINDER: {reminder}\n")


# ------------------------------------------
# Clipboard Manager
# ------------------------------------------

def clipboard_manager():
    text = pyperclip.paste()

    with open("clipboard_history.txt", "a") as file:
        file.write(text + "\n")

    print("✅ Clipboard content saved.\n")
    print("Copied Text:", text)


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n========== Daily Utility Toolkit ==========")
    print("1. Notes Saver")
    print("2. Auto Shutdown Timer")
    print("3. Cancel Shutdown")
    print("4. Alarm Clock")
    print("5. Reminder App")
    print("6. Clipboard Manager")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        notes_saver()

    elif choice == "2":
        shutdown_timer()

    elif choice == "3":
        cancel_shutdown()

    elif choice == "4":
        alarm_clock()

    elif choice == "5":
        reminder_app()

    elif choice == "6":
        clipboard_manager()

    elif choice == "7":
        print("👋 Exiting Toolkit...")
        break

    else:
        print("❌ Invalid choice. Try again.")