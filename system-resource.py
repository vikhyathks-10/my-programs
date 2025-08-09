import psutil
import time
import os

def show_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"🖥️ CPU Usage   : {cpu}%")
    print(f"💾 RAM Usage   : {memory}%")

print("🔁 Press Ctrl+C to stop monitoring.\n")

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
        print("📊 System Resource Monitor\n")
        show_stats()
        time.sleep(2)  # Refresh every 2 seconds
except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped.")
    print("Thank you for using the System Resource Monitor!")