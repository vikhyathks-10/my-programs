# 🔹 DAY 21 - MIXED AUTOMATION PRACTICE

import os
import shutil
import datetime
import time


# 🔹 1. Daily Backup System

def daily_backup(source_file):

    print("\n--- Daily Backup System ---")

    today = datetime.datetime.now().strftime("%Y%m%d")

    backup_name = f"{source_file}_{today}.backup"

    shutil.copy(source_file, backup_name)

    print("Backup Created:", backup_name)


# 🔹 2. Auto Cleanup Script

def cleanup_temp_files(path):

    print("\n--- Auto Cleanup Script ---")

    removed = 0

    for file in os.listdir(path):

        if file.endswith(".tmp") or file.endswith(".temp"):

            os.remove(file)

            removed += 1

            print("Deleted:", file)

    print("Total Removed:", removed)


# 🔹 3. Smart Folder Sorter

def smart_sorter(path):

    print("\n--- Smart Folder Sorter ---")

    for file in os.listdir(path):

        if os.path.isfile(file):

            ext = os.path.splitext(file)[1][1:]

            if ext == "":
                ext = "others"

            folder_name = ext.upper() + "_Files"

            if not os.path.exists(folder_name):
                os.mkdir(folder_name)

            shutil.move(file,
                        os.path.join(folder_name, file))

    print("Files Organized")


# 🔹 4. CLI Productivity Tool

def productivity_tool():

    print("\n--- CLI Productivity Tool ---")

    print("1. Show Current Time")
    print("2. Show Current Directory")
    print("3. List Files")

    choice = input("Enter Choice: ")

    if choice == "1":

        current_time = time.strftime("%H:%M:%S")

        print("Time:", current_time)

    elif choice == "2":

        print("Directory:", os.getcwd())

    elif choice == "3":

        for file in os.listdir():
            print(file)

    else:
        print("Invalid Choice")


# 🔹 5. Personal Assistant Basics

def personal_assistant():

    print("\n--- Personal Assistant ---")

    command = input("Ask something: ").lower()

    if "time" in command:

        print("Current Time:",
              time.strftime("%H:%M:%S"))

    elif "date" in command:

        print("Today's Date:",
              datetime.datetime.now().date())

    elif "files" in command:

        print("Files:")
        for file in os.listdir():
            print(file)

    else:
        print("Sorry, command not understood")


# 🔹 MAIN PROGRAM

# Create sample file
with open("notes.txt", "w") as f:
    f.write("Automation Practice")


daily_backup("notes.txt")


# Create temp files
with open("cache.tmp", "w") as f:
    f.write("temp")

with open("temp.temp", "w") as f:
    f.write("temporary")


cleanup_temp_files(".")


# ⚠️ Uncomment carefully
# smart_sorter(".")


productivity_tool()

personal_assistant()