import time

start_time = None
elapsed = 0

while True:
    print("\n1.Start  2.Stop  3.Reset  4.Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        start_time = time.time()
        print("Stopwatch started...")

    elif choice == '2':
        if start_time:
            elapsed += time.time() - start_time
            start_time = None
            print(f"Elapsed Time: {elapsed:.2f} seconds")

    elif choice == '3':
        start_time = None
        elapsed = 0
        print("Stopwatch reset.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")