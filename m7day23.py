# ==========================================================
# Month 7 - Day 23
# Concurrency in Python
#
# Topics Covered:
# 1. Multithreading
# 2. ThreadPoolExecutor
# 3. Multiprocessing
# 4. ProcessPoolExecutor
# 5. Async Programming (asyncio)
# 6. Thread vs Process vs Async
# ==========================================================

import threading
import multiprocessing
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# ==========================================================
# Functions
# ==========================================================

def download(name):
    print(f"{name} Started")
    time.sleep(2)
    print(f"{name} Completed")


def square(n):
    time.sleep(1)
    return n * n


def worker():
    print("Running in Separate Process")


def cube(n):
    return n ** 3


async def task(name, delay):
    print(f"{name} Started")
    await asyncio.sleep(delay)
    print(f"{name} Completed")


async def main_async():
    await asyncio.gather(
        task("Task-1", 2),
        task("Task-2", 1),
        task("Task-3", 3)
    )


# ==========================================================
# Demo Functions
# ==========================================================

def demo_multithreading():

    print("=" * 60)
    print("1. MULTITHREADING")
    print("=" * 60)

    t1 = threading.Thread(target=download, args=("File-1",))
    t2 = threading.Thread(target=download, args=("File-2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All Threads Finished")


def demo_threadpool():

    print("\n" + "=" * 60)
    print("2. THREAD POOL EXECUTOR")
    print("=" * 60)

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, [1, 2, 3, 4, 5])

    print("Squares:")

    for result in results:
        print(result)


def demo_multiprocessing():

    print("\n" + "=" * 60)
    print("3. MULTIPROCESSING")
    print("=" * 60)

    process = multiprocessing.Process(target=worker)

    process.start()
    process.join()

    print("Process Completed")


def demo_processpool():

    print("\n" + "=" * 60)
    print("4. PROCESS POOL EXECUTOR")
    print("=" * 60)

    with ProcessPoolExecutor() as executor:
        results = executor.map(cube, [1, 2, 3, 4, 5])

    print("Cubes:")

    for result in results:
        print(result)


def demo_async():

    print("\n" + "=" * 60)
    print("5. ASYNC PROGRAMMING")
    print("=" * 60)

    asyncio.run(main_async())


def demo_comparison():

    print("\n" + "=" * 60)
    print("6. THREAD vs PROCESS vs ASYNC")
    print("=" * 60)

    print("""
Threads
--------
✔ Shared Memory
✔ Lightweight
✔ Best for I/O Tasks

Processes
----------
✔ Separate Memory
✔ Heavyweight
✔ Best for CPU Tasks

Async
------
✔ Single Thread
✔ Event Loop
✔ Best for Thousands of I/O Tasks
""")


def interview_summary():

    print("\n" + "=" * 60)
    print("INTERVIEW SUMMARY")
    print("=" * 60)

    print("""
✔ Multithreading

Module

threading

Best For

✔ File I/O
✔ Network Requests
✔ Database Calls

--------------------------------------------------

✔ ThreadPoolExecutor

Simplifies thread management.

Module

concurrent.futures

--------------------------------------------------

✔ Multiprocessing

Module

multiprocessing

Each process has
its own memory.

Best For

✔ CPU-intensive work

--------------------------------------------------

✔ ProcessPoolExecutor

Runs tasks across
multiple CPU cores.

--------------------------------------------------

✔ asyncio

Used for asynchronous
programming.

Keywords

async

await

--------------------------------------------------

Thread vs Process

Thread
✔ Shared Memory
✔ Fast Creation

Process
✔ Separate Memory
✔ True Parallelism

--------------------------------------------------

When to Use What?

Download Files
→ Threads

Image Processing
→ Processes

Web APIs
→ Asyncio

--------------------------------------------------

Python GIL

Global Interpreter Lock

• One thread executes Python bytecode
  at a time.

• Threads are ideal for I/O-bound tasks.

• Processes are preferred for CPU-bound tasks.

--------------------------------------------------

Most Asked Interview Questions

✔ Thread vs Process

✔ ThreadPoolExecutor

✔ ProcessPoolExecutor

✔ asyncio

✔ async vs await

✔ GIL

✔ CPU-bound vs I/O-bound
""")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    multiprocessing.freeze_support()

    demo_multithreading()

    demo_threadpool()

    demo_multiprocessing()

    demo_processpool()

    demo_async()

    demo_comparison()

    interview_summary()