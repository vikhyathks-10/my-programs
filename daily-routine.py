import time
from datetime import datetime

# Task list (add as needed)
reminders = {
    "16:00": "Drink water ",
    "19:00": "Go for a walk ",
    "21:00": "Study Python "
}

print("Reminder started... Press Ctrl+C to stop.\n")

while True:
    now = datetime.now().strftime("%H:%M")
    if now in reminders:
        print(f" Reminder: {reminders[now]}")
        time.sleep(60)  # Wait to avoid repeating same minute
    time.sleep(10)  # Check every 10 seconds
