"""
MONTH 11 - DAY 8
GREEDY ALGORITHM FUNDAMENTALS

Programs:
36. Activity Selection Problem
37. Fractional Knapsack Problem
38. Minimum Number of Coins using Greedy
39. Job Sequencing with Deadlines
40. Assign Cookies

Menu:
36-40: Run individual programs
41: Run all programs
0: Exit
"""

from typing import Optional


# ---------------------------------------------------------
# PROGRAM 36: ACTIVITY SELECTION PROBLEM
# ---------------------------------------------------------

def activity_selection(
    activities: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Select the maximum number of non-overlapping activities.

    Each activity is represented as (start_time, finish_time).
    Activities are considered compatible when the next start
    time is greater than or equal to the previous finish time.
    """

    # Sort activities by their finishing times.
    sorted_activities = sorted(
        activities,
        key=lambda activity: activity[1]
    )

    selected: list[tuple[int, int]] = []
    last_finish = float("-inf")

    for start, finish in sorted_activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


def program_36() -> None:
    print("\nPROGRAM 36: ACTIVITY SELECTION")

    activities = [
        (1, 3),
        (2, 5),
        (4, 6),
        (6, 7),
        (5, 8),
        (8, 9)
    ]

    print("Activities (start, finish):", activities)

    selected = activity_selection(activities)

    print("Selected activities:", selected)
    print("Maximum number of activities:", len(selected))


# ---------------------------------------------------------
# PROGRAM 37: FRACTIONAL KNAPSACK
# ---------------------------------------------------------

def fractional_knapsack(
    items: list[tuple[float, float]],
    capacity: float
) -> tuple[float, list[tuple[int, float, float]]]:
    """
    Maximize profit by selecting whole or fractional items.

    Each item is represented as (weight, value).

    Returns:
        (maximum_profit, selected_items)

    Each selected item is represented as:
        (item_index, weight_taken, profit_earned)
    """

    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")

    for weight, value in items:
        if weight <= 0:
            raise ValueError("Item weights must be positive.")
        if value < 0:
            raise ValueError("Item values cannot be negative.")

    # Sort items by value-to-weight ratio, highest first.
    sorted_items = sorted(
        enumerate(items),
        key=lambda entry: entry[1][1] / entry[1][0],
        reverse=True
    )

    remaining_capacity = capacity
    total_profit = 0.0

    selected: list[tuple[int, float, float]] = []

    for index, (weight, value) in sorted_items:
        if remaining_capacity <= 0:
            break

        weight_taken = min(weight, remaining_capacity)
        profit_earned = (value / weight) * weight_taken

        total_profit += profit_earned
        remaining_capacity -= weight_taken

        selected.append((index, weight_taken, profit_earned))

    return total_profit, selected


def program_37() -> None:
    print("\nPROGRAM 37: FRACTIONAL KNAPSACK")

    items = [
        (10.0, 60.0),
        (20.0, 100.0),
        (30.0, 120.0)
    ]

    capacity = 50.0

    print("Items (weight, value):", items)
    print("Knapsack capacity:", capacity)

    profit, selected = fractional_knapsack(items, capacity)

    print("\nSelected items:")

    for index, weight_taken, profit_earned in selected:
        print(
            f"Item {index + 1}: "
            f"Weight taken = {weight_taken:.2f}, "
            f"Profit = {profit_earned:.2f}"
        )

    print(f"\nMaximum profit: {profit:.2f}")


# ---------------------------------------------------------
# PROGRAM 38: MINIMUM NUMBER OF COINS USING GREEDY
# ---------------------------------------------------------

def minimum_coins_greedy(
    coins: list[int],
    amount: int
) -> Optional[list[int]]:
    """
    Find coins using the greedy approach.

    This approach is guaranteed to give an optimal answer
    only for suitable coin systems (canonical systems).

    Returns None if the amount cannot be formed.
    """

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if any(coin <= 0 for coin in coins):
        raise ValueError("Coin denominations must be positive.")

    remaining = amount
    result: list[int] = []

    # Choose the largest available denomination first.
    for coin in sorted(set(coins), reverse=True):
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining != 0:
        return None

    return result


def program_38() -> None:
    print("\nPROGRAM 38: MINIMUM NUMBER OF COINS USING GREEDY")

    coins = [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    amount = 93

    print("Coin denominations:", coins)
    print("Amount:", amount)

    result = minimum_coins_greedy(coins, amount)

    if result is not None:
        print("Coins selected:", result)
        print("Minimum coins using greedy:", len(result))
    else:
        print("The amount cannot be formed using these coins.")


# ---------------------------------------------------------
# PROGRAM 39: JOB SEQUENCING WITH DEADLINES
# ---------------------------------------------------------

def job_sequencing(
    jobs: list[tuple[str, int, int]]
) -> tuple[list[tuple[str, int, int]], int]:
    """
    Schedule jobs to maximize profit.

    Each job is represented as:
        (job_id, deadline, profit)

    Every job takes exactly one time slot.
    Deadlines are positive integers.
    """

    for job_id, deadline, profit in jobs:
        if deadline < 1:
            raise ValueError(
                f"Job {job_id} must have a positive deadline."
            )
        if profit < 0:
            raise ValueError(
                f"Job {job_id} cannot have negative profit."
            )

    # Sort jobs by profit in descending order.
    sorted_jobs = sorted(
        jobs,
        key=lambda job: job[2],
        reverse=True
    )

    if not sorted_jobs:
        return [], 0

    max_deadline = max(job[1] for job in sorted_jobs)

    # Each position represents one time slot.
    slots: list[Optional[tuple[str, int, int]]] = [
        None
    ] * (max_deadline + 1)

    total_profit = 0

    for job in sorted_jobs:
        job_id, deadline, profit = job

        # Find the latest available slot before the deadline.
        for slot in range(deadline, 0, -1):
            if slots[slot] is None:
                slots[slot] = job
                total_profit += profit
                break

    scheduled_jobs = [
        job for job in slots[1:]
        if job is not None
    ]

    return scheduled_jobs, total_profit


def program_39() -> None:
    print("\nPROGRAM 39: JOB SEQUENCING WITH DEADLINES")

    jobs = [
        ("A", 2, 100),
        ("B", 1, 19),
        ("C", 2, 27),
        ("D", 1, 25),
        ("E", 3, 15)
    ]

    print("Jobs (ID, deadline, profit):")

    for job in jobs:
        print(job)

    scheduled, total_profit = job_sequencing(jobs)

    print("\nScheduled jobs:")

    for slot, job in enumerate(scheduled, start=1):
        print(f"Time slot {slot}: Job {job[0]} (Profit: {job[2]})")

    print("Total jobs completed:", len(scheduled))
    print("Maximum profit:", total_profit)


# ---------------------------------------------------------
# PROGRAM 40: ASSIGN COOKIES
# ---------------------------------------------------------

def assign_cookies(
    greed: list[int],
    cookies: list[int]
) -> tuple[int, list[tuple[int, int]]]:
    """
    Maximize the number of satisfied children.

    A child is satisfied when the assigned cookie size
    is greater than or equal to the child's greed factor.

    Returns:
        (number_of_satisfied_children, assignments)

    Each assignment is (child_greed, cookie_size).
    """

    if any(value < 0 for value in greed):
        raise ValueError("Greed factors cannot be negative.")

    if any(value < 0 for value in cookies):
        raise ValueError("Cookie sizes cannot be negative.")

    sorted_greed = sorted(greed)
    sorted_cookies = sorted(cookies)

    child = 0
    cookie = 0

    assignments: list[tuple[int, int]] = []

    while child < len(sorted_greed) and cookie < len(sorted_cookies):

        if sorted_cookies[cookie] >= sorted_greed[child]:
            assignments.append(
                (sorted_greed[child], sorted_cookies[cookie])
            )
            child += 1

        # Use the cookie and move to the next one.
        cookie += 1

    return len(assignments), assignments


def program_40() -> None:
    print("\nPROGRAM 40: ASSIGN COOKIES")

    greed = [1, 2, 3]
    cookies = [1, 1]

    print("Children's greed factors:", greed)
    print("Cookie sizes:", cookies)

    count, assignments = assign_cookies(greed, cookies)

    print("\nCookie assignments:")

    for child_greed, cookie_size in assignments:
        print(
            f"Child with greed {child_greed} "
            f"receives cookie of size {cookie_size}"
        )

    print("\nMaximum satisfied children:", count)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 8: GREEDY FUNDAMENTALS")
        print("========================================")
        print("36. Activity Selection")
        print("37. Fractional Knapsack")
        print("38. Minimum Coins using Greedy")
        print("39. Job Sequencing with Deadlines")
        print("40. Assign Cookies")
        print("41. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 36:
            program_36()
        elif choice == 37:
            program_37()
        elif choice == 38:
            program_38()
        elif choice == 39:
            program_39()
        elif choice == 40:
            program_40()
        elif choice == 41:
            for program in (
                program_36,
                program_37,
                program_38,
                program_39,
                program_40
            ):
                program()
        elif choice == 0:
            print("Exiting Day 8 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 36-41.")


if __name__ == "__main__":
    main()