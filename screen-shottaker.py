import pyautogui
import time
from datetime import datetime
import os
delay = 3
print(f"⏳ Taking screenshot in {delay} seconds...")
time.sleep(delay)
screenshot = pyautogui.screenshot()
folder = "screenshots"
os.makedirs(folder, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = os.path.join(folder, f"screenshot_{timestamp}.png")

screenshot.save(file_path)

print(f"✅ Screenshot saved as {file_path}")
print("Thank you for using the Screenshot Tool!")