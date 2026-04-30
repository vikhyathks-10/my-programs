# 🔹 DAY 30 - FINAL BOSS PROJECT

#  OOP + DS SYSTEM (Task Manager)
class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        self.tasks.append(Task(name, priority))

    def show_tasks(self):
        # Priority sort (optimization)
        self.tasks.sort(key=lambda x: x.priority)
        for t in self.tasks:
            print(f"{t.name} (Priority {t.priority})")


#
def subset_sum(arr, index, target):
    if target == 0:
        return True
    if index == len(arr):
        return False

    return (subset_sum(arr, index+1, target-arr[index]) or
            subset_sum(arr, index+1, target))


# 🔥 PART 3: STACK + OPTIMIZATION (Largest Rectangle in Histogram)
def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area


# 🔥 PART 4: QUEUE + PROBLEM (Sliding Window Maximum)
from collections import deque

def max_sliding_window(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# 🔥 PART 5: MOCK INTERVIEW QUESTION (Merge Intervals)
def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


# 🔹 MAIN PROGRAM

print("\n🔥 --- TASK MANAGER (OOP + DS) ---")
tm = TaskManager()
tm.add_task("Study DSA", 2)
tm.add_task("Workout", 1)
tm.add_task("Project", 3)
tm.show_tasks()


print("\n🔥 --- SUBSET SUM (Recursion + DS) ---")
print(subset_sum([2, 4, 6, 8], 0, 10))


print("\n🔥 --- LARGEST RECTANGLE ---")
print(largest_rectangle([2, 1, 5, 6, 2, 3]))


print("\n🔥 --- SLIDING WINDOW MAX ---")
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))


print("\n🔥 --- MERGE INTERVALS ---")
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))