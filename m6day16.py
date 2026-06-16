# 🔹 DAY 16 - TO DO APP

import os


class TodoApp:

    FILE_NAME = "tasks.txt"

    # ==========================================
    # 🔹 Load Tasks
    # ==========================================

    def load_tasks(self):

        tasks = []

        if os.path.exists(self.FILE_NAME):

            with open(self.FILE_NAME, "r") as file:

                for line in file:

                    tasks.append(
                        line.strip().split("|")
                    )

        return tasks

    # ==========================================
    # 🔹 Save Tasks
    # ==========================================

    def save_tasks(self, tasks):

        with open(self.FILE_NAME, "w") as file:

            for task in tasks:

                file.write(
                    f"{task[0]}|{task[1]}\n"
                )

    # ==========================================
    # 🔹 Add Task
    # ==========================================

    def add_task(self):

        task_name = input(
            "Enter Task: "
        )

        tasks = self.load_tasks()

        tasks.append(
            [task_name, "Pending"]
        )

        self.save_tasks(tasks)

        print("✅ Task Added")

    # ==========================================
    # 🔹 View Tasks
    # ==========================================

    def view_tasks(self):

        tasks = self.load_tasks()

        if not tasks:

            print("No Tasks Found")
            return

        print("\n===== TASK LIST =====")

        for i, task in enumerate(tasks):

            print(
                f"{i+1}. {task[0]} "
                f"({task[1]})"
            )

    # ==========================================
    # 🔹 Delete Task
    # ==========================================

    def delete_task(self):

        tasks = self.load_tasks()

        if not tasks:

            print("No Tasks Found")
            return

        self.view_tasks()

        task_no = int(
            input(
                "\nEnter Task Number To Delete: "
            )
        )

        if 1 <= task_no <= len(tasks):

            tasks.pop(task_no - 1)

            self.save_tasks(tasks)

            print("✅ Task Deleted")

        else:

            print("Invalid Task Number")

    # ==========================================
    # 🔹 Mark Completed
    # ==========================================

    def mark_completed(self):

        tasks = self.load_tasks()

        if not tasks:

            print("No Tasks Found")
            return

        self.view_tasks()

        task_no = int(
            input(
                "\nEnter Task Number To Complete: "
            )
        )

        if 1 <= task_no <= len(tasks):

            tasks[task_no - 1][1] = "Completed"

            self.save_tasks(tasks)

            print("✅ Task Completed")

        else:

            print("Invalid Task Number")


# ==========================================
# 🔹 MAIN PROGRAM
# ==========================================

todo = TodoApp()

while True:

    print("\n===== TO-DO APP =====")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Completed")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        todo.add_task()

    elif choice == "2":

        todo.view_tasks()

    elif choice == "3":

        todo.delete_task()

    elif choice == "4":

        todo.mark_completed()

    elif choice == "5":

        print("Goodbye 👋")

        break

    else:

        print("Invalid Choice")