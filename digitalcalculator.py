import time
print("Press Ctrl+C to stop the clock.\n")

try:
    while True:
        current_time = time.strftime("%H:%M:%S")
        print("Time:", current_time, end="\r")  
        time.sleep(1)
except:
    print("\nClock stopped.")
