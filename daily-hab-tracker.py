from datetime import datetime
import os
today = datetime.now().strftime("%Y-%m-%d")
habits = input("Enter your habits for today (comma-separated): ").split(',')
statuses = {}
for habit in habits:
    habit = habit.strip()
    status = input(f"Did you complete '{habit}'? (yes/no): ").strip().lower()
    statuses[habit] = "✅ Done" if status == "yes" else "❌ Not Done"


folder = "habit_logs"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, f"{today}.txt")

with open(file_path, "w", encoding="utf-8") as file:

    file.write(f"Habit Tracker - {today}\n\n")
    for habit, status in statuses.items():
        file.write(f"{habit}: {status}\n")

print(f"\n📁 Log saved as {file_path}")
print("Thank you for using the Daily Habit Tracker!")