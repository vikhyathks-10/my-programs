# 🔹 DAY 4 - TIME MODULE

import time


# 🔹 1. Digital Clock

print("\n--- Digital Clock ---")

for i in range(5):   # runs 5 times
    current_time = time.strftime("%H:%M:%S")
    print("Current Time:", current_time)
    time.sleep(1)


# 🔹 2. Stopwatch

print("\n--- Stopwatch ---")

start = time.time()

time.sleep(2)   # simulate task

end = time.time()

print("Elapsed Time:", round(end - start, 2), "seconds")


# 🔹 3. Delay Execution using sleep()

print("\n--- Sleep Example ---")

print("Program starts...")
time.sleep(3)
print("Program resumed after 3 seconds")


# 🔹 4. Measure Execution Time

print("\n--- Execution Time ---")

start_time = time.time()

total = 0
for i in range(1000000):
    total += i

end_time = time.time()

print("Execution Time:",
      round(end_time - start_time, 4), "seconds")


# 🔹 5. Countdown Timer

print("\n--- Countdown Timer ---")

seconds = 5

while seconds > 0:
    print("Time Left:", seconds)
    time.sleep(1)
    seconds -= 1

print("Time's Up!")