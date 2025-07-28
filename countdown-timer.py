import time

seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds // 60
    secs = seconds % 60
    print(f"Time left: {mins:02d}:{secs:02d}")
    time.sleep(1)
    seconds -= 1

print("ime's up!")
