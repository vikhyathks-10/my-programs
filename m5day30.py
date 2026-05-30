#  DAY 30 - FINAL BOSS PROJECT

import os
import shutil
from datetime import datetime


# ==================================================
# 🔹 SMART FILE MANAGER
# ==================================================

class SmartFileManager:

    def __init__(self, path="."):
        self.path = path

    def organize_files(self):

        print("\n--- Organizing Files ---")

        for file in os.listdir(self.path):

            if os.path.isfile(file):

                ext = os.path.splitext(file)[1][1:]

                if ext == "":
                    ext = "others"

                folder = ext.upper() + "_Files"

                if not os.path.exists(folder):
                    os.mkdir(folder)

                shutil.move(file,
                            os.path.join(folder, file))

        print("Files Organized Successfully")

    def show_statistics(self):

        print("\n--- Folder Statistics ---")

        total_files = 0

        for root, dirs, files in os.walk(self.path):
            total_files += len(files)

        print("Total Files:", total_files)


# ==================================================
# 🔹 INTERVIEW CODING SET
# ==================================================

def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):

        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []


def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


# ==================================================
# 🔹 REAL-WORLD SIMULATION
# OFFICE TASK TRACKER
# ==================================================

class TaskManager:

    def __init__(self):

        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)

    def complete_task(self):

        if self.tasks:

            task = self.tasks.pop(0)

            print("Completed:", task)

        else:
            print("No Tasks Available")

    def show_tasks(self):

        print("\nPending Tasks:")

        if not self.tasks:
            print("No Pending Tasks")

        for task in self.tasks:
            print("-", task)


# ==================================================
# 🔹 REPORT GENERATOR
# ==================================================

def generate_report():

    report_name = (
        "report_" +
        datetime.now().strftime("%Y%m%d") +
        ".txt"
    )

    with open(report_name, "w") as file:

        file.write("FINAL BOSS REPORT\n")
        file.write("=================\n")
        file.write(
            "Project Executed Successfully\n"
        )

    print("\nReport Generated:", report_name)


# ==================================================
# 🔹 MAIN APP
# ==================================================

print("🔥 FINAL BOSS DAY PROJECT 🔥")

manager = SmartFileManager()
manager.organize_files()
manager.show_statistics()


print("\n--- Interview Coding Set ---")

print(
    "Two Sum:",
    two_sum([2, 7, 11, 15], 9)
)

print(
    "Binary Search:",
    binary_search([1, 3, 5, 7, 9], 7)
)


print("\n--- Task Manager ---")

tasks = TaskManager()

tasks.add_task("Finish Python Roadmap")
tasks.add_task("Build Portfolio")
tasks.add_task("Practice LeetCode")

tasks.show_tasks()

tasks.complete_task()

tasks.show_tasks()


generate_report()