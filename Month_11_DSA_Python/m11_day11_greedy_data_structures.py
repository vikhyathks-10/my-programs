
"""
MONTH 11 - DAY 11
GREEDY WITH DATA STRUCTURES

Programs:
51. Connect Ropes with Minimum Cost using Min Heap
52. Rearrange Characters so No Two Adjacent Are Same
53. Minimum Refuelling Stops
54. Maximum Profit CPU Job Scheduling
55. Minimum Cost to Hire K Workers

Menu:
51-55: Run individual programs
56: Run all programs
0: Exit
"""

import heapq
from collections import Counter
from typing import Optional


# ---------------------------------------------------------
# PROGRAM 51: CONNECT ROPES WITH MINIMUM COST
# ---------------------------------------------------------

def minimum_rope_connection_cost(ropes: list[int]) -> int:
    """
    Connect all ropes with minimum total cost.

    Connecting two ropes costs the sum of their lengths.
    A min heap always selects the two shortest ropes.
    """

    if any(length < 0 for length in ropes):
        raise ValueError("Rope lengths cannot be negative.")

    if len(ropes) <= 1:
        return 0

    min_heap = ropes.copy()
    heapq.heapify(min_heap)

    total_cost = 0

    while len(min_heap) > 1:
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)

        combined = first + second
        total_cost += combined

        heapq.heappush(min_heap, combined)

    return total_cost


def program_51() -> None:
    print("\nPROGRAM 51: CONNECT ROPES WITH MINIMUM COST")

    ropes = [4, 3, 2, 6]

    print("Rope lengths:", ropes)

    result = minimum_rope_connection_cost(ropes)

    print("Minimum connection cost:", result)


# ---------------------------------------------------------
# PROGRAM 52: REARRANGE CHARACTERS
# SO NO TWO ADJACENT CHARACTERS ARE SAME
# ---------------------------------------------------------

def rearrange_characters(text: str) -> str:
    """
    Rearrange characters so that no two adjacent characters
    are identical.

    Return an empty string if no valid arrangement exists.
    """

    if not text:
        return ""

    frequencies = Counter(text)

    # A valid arrangement is impossible if one character
    # occurs more than (n + 1) // 2 times.
    maximum_frequency = max(frequencies.values())

    if maximum_frequency > (len(text) + 1) // 2:
        return ""

    # Python heapq is a min heap, so use negative frequencies.
    max_heap = [
        (-frequency, character)
        for character, frequency in frequencies.items()
    ]

    heapq.heapify(max_heap)

    result: list[str] = []

    # Hold the previously used character out of the heap
    # until another character has been selected.
    previous: Optional[tuple[int, str]] = None

    while max_heap:
        negative_frequency, character = heapq.heappop(max_heap)

        result.append(character)

        # Reinsert the previously used character.
        if previous is not None:
            heapq.heappush(max_heap, previous)

        remaining_frequency = negative_frequency + 1

        if remaining_frequency < 0:
            previous = (remaining_frequency, character)
        else:
            previous = None

    rearranged = "".join(result)

    # Defensive verification.
    for index in range(1, len(rearranged)):
        if rearranged[index] == rearranged[index - 1]:
            return ""

    return rearranged


def program_52() -> None:
    print("\nPROGRAM 52: REARRANGE CHARACTERS")

    text = "aaabbc"

    print("Original string:", text)

    result = rearrange_characters(text)

    if result:
        print("Rearranged string:", result)
    else:
        print("A valid rearrangement is not possible.")


# ---------------------------------------------------------
# PROGRAM 53: MINIMUM REFUELLING STOPS
# ---------------------------------------------------------

def minimum_refuelling_stops(
    target: int,
    start_fuel: int,
    stations: list[tuple[int, int]]
) -> int:
    """
    Find the minimum number of refuelling stops needed
    to reach the target.

    Each station is represented as:
        (position, fuel_available)

    A max heap stores fuel amounts from stations already
    passed but not yet selected for refuelling.

    Return -1 if the destination cannot be reached.
    """

    if target < 0 or start_fuel < 0:
        raise ValueError("Target and starting fuel cannot be negative.")

    if any(position < 0 or fuel < 0 for position, fuel in stations):
        raise ValueError("Station positions and fuel cannot be negative.")

    if any(
        stations[i][0] > stations[i + 1][0]
        for i in range(len(stations) - 1)
    ):
        raise ValueError("Stations must be sorted by position.")

    if start_fuel >= target:
        return 0

    max_heap: list[int] = []

    current_fuel = start_fuel
    current_position = 0
    stops = 0

    for position, fuel in stations + [(target, 0)]:

        distance_to_next = position - current_position
        current_fuel -= distance_to_next

        # Refuel using the largest previously available station
        # whenever the next destination cannot be reached.
        while current_fuel < 0 and max_heap:
            current_fuel += -heapq.heappop(max_heap)
            stops += 1

        if current_fuel < 0:
            return -1

        # The station has now been reached.
        heapq.heappush(max_heap, -fuel)
        current_position = position

    return stops


def program_53() -> None:
    print("\nPROGRAM 53: MINIMUM REFUELLING STOPS")

    target = 100
    start_fuel = 10

    stations = [
        (10, 60),
        (20, 30),
        (30, 30),
        (60, 40)
    ]

    print("Destination:", target)
    print("Starting fuel:", start_fuel)
    print("Stations (position, fuel):", stations)

    result = minimum_refuelling_stops(
        target,
        start_fuel,
        stations
    )

    if result != -1:
        print("Minimum refuelling stops:", result)
    else:
        print("Destination cannot be reached.")


# ---------------------------------------------------------
# PROGRAM 54: MAXIMUM PROFIT CPU JOB SCHEDULING
# ---------------------------------------------------------

def schedule_maximum_profit_jobs(
    jobs: list[tuple[str, int, int]]
) -> tuple[int, list[tuple[str, int, int]]]:
    """
    Select unit-time jobs to maximize total profit.

    Each job is represented as:
        (job_id, deadline, profit)

    Every job requires exactly one time unit.
    A job must be completed no later than its deadline.

    Returns:
        (maximum_profit, selected_jobs)

    A min heap removes the least profitable selected job
    whenever the selected count exceeds the current deadline.
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

    # Sort jobs by deadline.
    sorted_jobs = sorted(
        jobs,
        key=lambda job: job[1]
    )

    # Heap entries: (profit, job_id, deadline)
    min_heap: list[tuple[int, str, int]] = []

    total_profit = 0

    for job_id, deadline, profit in sorted_jobs:
        heapq.heappush(
            min_heap,
            (profit, job_id, deadline)
        )

        total_profit += profit

        # At most 'deadline' unit-time jobs can be completed
        # by this deadline.
        if len(min_heap) > deadline:
            removed_profit, _, _ = heapq.heappop(min_heap)
            total_profit -= removed_profit

    selected_jobs = [
        (job_id, deadline, profit)
        for profit, job_id, deadline in min_heap
    ]

    selected_jobs.sort(key=lambda job: job[1])

    return total_profit, selected_jobs


def program_54() -> None:
    print("\nPROGRAM 54: MAXIMUM PROFIT CPU JOB SCHEDULING")

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

    total_profit, selected = schedule_maximum_profit_jobs(jobs)

    print("\nSelected jobs:")

    for job_id, deadline, profit in selected:
        print(
            f"Job {job_id}: Deadline = {deadline}, "
            f"Profit = {profit}"
        )

    print("Number of selected jobs:", len(selected))
    print("Maximum total profit:", total_profit)


# ---------------------------------------------------------
# PROGRAM 55: MINIMUM COST TO HIRE K WORKERS
# ---------------------------------------------------------

def minimum_cost_to_hire_workers(
    quality: list[int],
    wage: list[int],
    k: int
) -> tuple[float, list[int]]:
    """
    Hire exactly k workers with minimum total cost.

    Each worker is represented by:
        quality[i]
        wage[i]

    Every hired worker must receive at least their
    minimum wage expectation.

    The selected workers are returned as 1-based indices.
    """

    n = len(quality)

    if len(wage) != n:
        raise ValueError(
            "Quality and wage arrays must have equal lengths."
        )

    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and the number of workers.")

    if any(value <= 0 for value in quality):
        raise ValueError("Worker quality must be positive.")

    if any(value < 0 for value in wage):
        raise ValueError("Worker wages cannot be negative.")

    # Each entry contains:
    # (minimum wage / quality ratio, quality, worker index)
    workers = sorted(
        (
            wage[i] / quality[i],
            quality[i],
            i
        )
        for i in range(n)
    )

    # Max heap of selected qualities, represented by negatives.
    quality_heap: list[int] = []

    quality_sum = 0
    minimum_cost = float("inf")
    best_worker_indices: list[int] = []

    for ratio, worker_quality, worker_index in workers:

        heapq.heappush(quality_heap, -worker_quality)
        quality_sum += worker_quality

        # Keep only the k workers with the smallest qualities.
        if len(quality_heap) > k:
            removed_quality = -heapq.heappop(quality_heap)
            quality_sum -= removed_quality

        if len(quality_heap) == k:
            current_cost = ratio * quality_sum

            if current_cost < minimum_cost:
                minimum_cost = current_cost

                # Recover the selected worker indices.
                best_worker_indices = [
                    index + 1
                    for worker_ratio, worker_q, index in workers
                    if worker_ratio <= ratio
                    and -worker_q in quality_heap
                ]

                # A worker may have the same quality as another.
                # Reconstruct the exact selected workers below.
                selected_qualities = Counter(
                    -value for value in quality_heap
                )

                best_worker_indices = []

                for previous_ratio, previous_quality, previous_index in workers:
                    if previous_ratio > ratio:
                        break

                    if selected_qualities[previous_quality] > 0:
                        best_worker_indices.append(previous_index + 1)
                        selected_qualities[previous_quality] -= 1

    return minimum_cost, sorted(best_worker_indices)


def program_55() -> None:
    print("\nPROGRAM 55: MINIMUM COST TO HIRE K WORKERS")

    quality = [10, 20, 5]
    wage = [70, 50, 30]
    k = 2

    print("Worker qualities:", quality)
    print("Minimum wage expectations:", wage)
    print("Workers to hire:", k)

    minimum_cost, selected_workers = minimum_cost_to_hire_workers(
        quality,
        wage,
        k
    )

    print("Selected worker indices:", selected_workers)
    print(f"Minimum hiring cost: {minimum_cost:.2f}")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 11: GREEDY WITH HEAPS")
        print("========================================")
        print("51. Connect Ropes with Minimum Cost")
        print("52. Rearrange Characters")
        print("53. Minimum Refuelling Stops")
        print("54. Maximum Profit CPU Job Scheduling")
        print("55. Minimum Cost to Hire K Workers")
        print("56. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 51:
            program_51()
        elif choice == 52:
            program_52()
        elif choice == 53:
            program_53()
        elif choice == 54:
            program_54()
        elif choice == 55:
            program_55()
        elif choice == 56:
            for program in (
                program_51,
                program_52,
                program_53,
                program_54,
                program_55
            ):
                program()
        elif choice == 0:
            print("Exiting Day 11 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 51-56.")


if __name__ == "__main__":
    main()
