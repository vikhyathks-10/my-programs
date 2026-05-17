# 🔹 DAY 17 - LOGGING & REPORTS

import logging
import time
import os
from datetime import datetime


# 🔹 Configure Logging

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# 🔹 1. Log File Generator

def generate_log():

    print("\n--- Log File Generator ---")

    logging.info("System started")
    logging.warning("Low memory warning")
    logging.error("Sample error occurred")

    print("Logs Written to system.log")


# 🔹 2. Login Activity Tracker

def login_tracker(username):

    print("\n--- Login Activity Tracker ---")

    logging.info(f"User '{username}' logged in")

    print("Login Activity Saved")


# 🔹 3. Error Logger

def divide(a, b):

    try:
        result = a / b
        return result

    except Exception as e:

        logging.error(f"Error: {e}")

        return "Error Logged"


# 🔹 4. System Usage Report

def system_report():

    print("\n--- System Usage Report ---")

    files = len(os.listdir("."))

    current_time = datetime.now()

    report = f"""
SYSTEM REPORT
--------------
Time: {current_time}
Files in Current Directory: {files}
"""

    print(report)

    logging.info("System report generated")


# 🔹 5. Daily Report Generator

def daily_report():

    print("\n--- Daily Report Generator ---")

    today = datetime.now().strftime("%Y-%m-%d")

    report_name = f"report_{today}.txt"

    with open(report_name, "w") as f:

        f.write("DAILY REPORT\n")
        f.write("-----------------\n")
        f.write(f"Generated On: {today}\n")
        f.write("System running normally.\n")

    print("Daily Report Created:", report_name)

    logging.info("Daily report created")


# 🔹 MAIN PROGRAM

generate_log()

login_tracker("Vikyat")

print(divide(10, 0))

system_report()

daily_report()