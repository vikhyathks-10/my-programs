
# ============================================================
# MONTH 11 - DAY 14
# WEEK 2 REVISION
# Programs 66-70
# ============================================================

from typing import Optional
import heapq
from bisect import bisect_left


# ============================================================
# PROGRAM 66: MINIMUM MEETING ROOMS
# ============================================================

def minimum_meeting_rooms(meetings: list[tuple[int, int]]) -> int:
    """
    Find the minimum number of rooms required for all meetings.

    Each meeting is represented as (start, end).
    A room can be reused when the previous meeting ends
    at or before the next meeting starts.
    """

    if any(start >= end for start, end in meetings):
        raise ValueError("Every meeting must have start < end.")

    if not meetings:
        return 0

    meetings = sorted(meetings)

    # Min heap stores the ending times of occupied rooms.
    ending_times: list[int] = []

    for start, end in meetings:

        # Release rooms whose meetings have already ended.
        while ending_times and ending_times[0] <= start:
            heapq.heappop(ending_times)

        heapq.heappush(ending_times, end)

    return len(ending_times)


def run_program_66() -> None:
    print("\n--- PROGRAM 66: MINIMUM MEETING ROOMS ---")

    count = int(input("Enter number of meetings: "))

    meetings: list[tuple[int, int]] = []

    for index in range(count):
        start, end = map(
            int,
            input(f"Enter start and end of meeting {index + 1}: ").split()
        )
        meetings.append((start, end))

    result = minimum_meeting_rooms(meetings)

    print("Minimum meeting rooms required:", result)


# ============================================================
# PROGRAM 67: WEIGHTED INTERVAL SCHEDULING
# BRUTE FORCE VS GREEDY
# ============================================================

def weighted_schedule_brute_force(
    activities: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Find the maximum total weight of non-overlapping activities.

    Each activity is (start, end, weight).

    This recursive brute-force solution explores both choices:
    1. Select the current activity.
    2. Skip the current activity.

    It returns the optimal total weight and selected activities.
    """

    if any(start >= end for start, end, _ in activities):
        raise ValueError("Every activity must have start < end.")

    activities = sorted(activities, key=lambda item: item[0])

    def solve(
        index: int
    ) -> tuple[int, list[tuple[int, int, int]]]:

        if index >= len(activities):
            return 0, []

        # Choice 1: Skip the current activity.
        skip_weight, skip_selection = solve(index + 1)

        # Choice 2: Select the current activity.
        start, end, weight = activities[index]

        next_index = index + 1

        while (
            next_index < len(activities)
            and activities[next_index][0] < end
        ):
            next_index += 1

        take_weight, take_selection = solve(next_index)

        take_weight += weight
        take_selection = [activities[index]] + take_selection

        if take_weight > skip_weight:
            return take_weight, take_selection

        return skip_weight, skip_selection

    return solve(0)


def weighted_schedule_greedy(
    activities: list[tuple[int, int, int]]
) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Greedy heuristic:
    Sort activities by descending weight and select an activity
    if it does not overlap with already selected activities.

    This is NOT guaranteed to produce the optimal answer.
    """

    if any(start >= end for start, end, _ in activities):
        raise ValueError("Every activity must have start < end.")

    sorted_activities = sorted(
        activities,
        key=lambda item: item[2],
        reverse=True
    )

    selected: list[tuple[int, int, int]] = []

    for activity in sorted_activities:
        start, end, _ = activity

        overlaps = any(
            start < selected_end and selected_start < end
            for selected_start, selected_end, _ in selected
        )

        if not overlaps:
            selected.append(activity)

    selected.sort(key=lambda item: item[0])

    total_weight = sum(weight for _, _, weight in selected)

    return total_weight, selected


def run_program_67() -> None:
    print("\n--- PROGRAM 67: WEIGHTED INTERVAL SCHEDULING ---")

    count = int(input("Enter number of activities: "))

    activities: list[tuple[int, int, int]] = []

    for index in range(count):
        start, end, weight = map(
            int,
            input(
                f"Enter start, end and priority of activity {index + 1}: "
            ).split()
        )

        activities.append((start, end, weight))

    brute_weight, brute_selection = weighted_schedule_brute_force(
        activities
    )

    greedy_weight, greedy_selection = weighted_schedule_greedy(
        activities
    )

    print("\nBrute-force optimal result:")
    print("Maximum total priority:", brute_weight)
    print("Selected activities:", brute_selection)

    print("\nGreedy heuristic result:")
    print("Total priority:", greedy_weight)
    print("Selected activities:", greedy_selection)

    if brute_weight == greedy_weight:
        print("\nBoth methods produced the same total priority.")
    else:
        print("\nGreedy did not produce the optimal total priority.")


# ============================================================
# PROGRAM 68: MINIMUM COINS FOR A CANONICAL COIN SYSTEM
# ============================================================

def minimum_coins_greedy(
    denominations: list[int],
    amount: int
) -> tuple[int, list[int]]:
    """
    Find the minimum number of coins using greedy.

    IMPORTANT:
    The supplied denominations must form a canonical coin system
    for greedy to guarantee the minimum number of coins.

    Example denominations:
    [1, 2, 5, 10, 20, 50, 100, 500, 2000]
    """

    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if not denominations:
        raise ValueError("Denominations cannot be empty.")

    if any(coin <= 0 for coin in denominations):
        raise ValueError("Coin denominations must be positive.")

    if len(set(denominations)) != len(denominations):
        raise ValueError("Coin denominations must be unique.")

    denominations = sorted(denominations, reverse=True)

    remaining = amount
    selected_coins: list[int] = []

    for coin in denominations:
        count = remaining // coin

        if count > 0:
            selected_coins.extend([coin] * count)
            remaining %= coin

    if remaining != 0:
        raise ValueError(
            "The supplied denominations cannot form this amount."
        )

    return len(selected_coins), selected_coins


def run_program_68() -> None:
    print("\n--- PROGRAM 68: CANONICAL COIN SYSTEM ---")

    denominations = list(
        map(
            int,
            input("Enter coin denominations: ").split()
        )
    )

    amount = int(input("Enter target amount: "))

    count, coins = minimum_coins_greedy(
        denominations,
        amount
    )

    print("Minimum number of coins:", count)
    print("Selected coins:", coins)


# ============================================================
# PROGRAM 69: SMALLEST MAXIMUM LOAD AMONG K WORKERS
# ============================================================

def can_distribute_jobs(
    jobs: list[int],
    workers: int,
    max_load: int
) -> bool:
    """
    Check whether jobs can be distributed among at most
    the given number of workers without exceeding max_load.

    Jobs must remain in their original order.
    Each worker receives a contiguous group of jobs.
    """

    required_workers = 1
    current_load = 0

    for job in jobs:
        if current_load + job <= max_load:
            current_load += job
        else:
            required_workers += 1
            current_load = job

    return required_workers <= workers


def minimum_maximum_load(
    jobs: list[int],
    workers: int
) -> Optional[int]:
    """
    Distribute jobs among workers while minimizing the
    maximum total load assigned to any worker.

    Each worker gets a contiguous, non-empty group of jobs.

    Returns None if workers > number of jobs.
    """

    if not jobs:
        raise ValueError("Job list cannot be empty.")

    if any(job < 0 for job in jobs):
        raise ValueError("Job durations cannot be negative.")

    if workers <= 0:
        raise ValueError("Number of workers must be positive.")

    if workers > len(jobs):
        return None

    left = max(jobs)
    right = sum(jobs)
    answer = right

    while left <= right:
        max_load = left + (right - left) // 2

        if can_distribute_jobs(jobs, workers, max_load):
            answer = max_load
            right = max_load - 1
        else:
            left = max_load + 1

    return answer


def run_program_69() -> None:
    print("\n--- PROGRAM 69: MINIMUM MAXIMUM WORKER LOAD ---")

    jobs = list(map(int, input("Enter job durations: ").split()))
    workers = int(input("Enter number of workers: "))

    result = minimum_maximum_load(jobs, workers)

    if result is None:
        print("Distribution is impossible.")
    else:
        print("Smallest possible maximum load:", result)


# ============================================================
# PROGRAM 70: MINIMUM MAXIMUM DISTANCE BETWEEN GAS STATIONS
# ============================================================

def stations_needed(
    positions: list[float],
    max_distance: float
) -> int:
    """
    Count the number of new stations required so that
    every gap between consecutive stations is <= max_distance.
    """

    required = 0

    for index in range(1, len(positions)):
        gap = positions[index] - positions[index - 1]

        if gap <= 0:
            continue

        # Number of stations needed inside this gap.
        ratio = gap / max_distance

        # Small tolerance helps avoid floating-point boundary errors.
        required += max(0, int(ratio - 1e-12 + 0.999999999999) - 1)

    return required


def minimize_max_gas_station_distance(
    positions: list[float],
    new_stations: int
) -> float:
    """
    Add at most new_stations to minimize the maximum distance
    between consecutive gas stations.

    Returns the minimum possible maximum distance.
    """

    if len(positions) < 2:
        raise ValueError("At least two existing stations are required.")

    if new_stations < 0:
        raise ValueError("Number of new stations cannot be negative.")

    positions = sorted(positions)

    if any(
        positions[index] == positions[index - 1]
        for index in range(1, len(positions))
    ):
        raise ValueError("Existing station positions must be distinct.")

    left = 0.0
    right = max(
        positions[index] - positions[index - 1]
        for index in range(1, len(positions))
    )

    # Fixed number of iterations gives sufficient precision.
    for _ in range(100):
        mid = (left + right) / 2

        if stations_needed(positions, mid) <= new_stations:
            right = mid
        else:
            left = mid

    return right


def run_program_70() -> None:
    print("\n--- PROGRAM 70: GAS STATION DISTANCE ---")

    positions = list(
        map(float, input("Enter existing station positions: ").split())
    )

    new_stations = int(input("Enter number of new stations: "))

    result = minimize_max_gas_station_distance(
        positions,
        new_stations
    )

    print("Minimum possible maximum distance:", round(result, 6))


# ============================================================
# RUN ALL PROGRAMS
# ============================================================

def run_all_programs() -> None:
    print("\n========== RUNNING ALL DAY 14 PROGRAMS ==========")

    run_program_66()
    run_program_67()
    run_program_68()
    run_program_69()
    run_program_70()


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:
    while True:
        print("\n==============================================")
        print("       MONTH 11 - DAY 14 DSA MENU")
        print("              WEEK 2 REVISION")
        print("==============================================")

        print("66. Minimum Meeting Rooms")
        print("67. Weighted Interval Scheduling")
        print("68. Minimum Coins - Canonical Coin System")
        print("69. Minimum Maximum Load Among Workers")
        print("70. Minimum Maximum Gas Station Distance")
        print("71. Run All Programs")
        print("0. Exit")

        print("==============================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 66:
                run_program_66()

            elif choice == 67:
                run_program_67()

            elif choice == 68:
                run_program_68()

            elif choice == 69:
                run_program_69()

            elif choice == 70:
                run_program_70()

            elif choice == 71:
                run_all_programs()

            elif choice == 0:
                print("Exiting Day 14 DSA Programs. Keep practicing!")
                break

            else:
                print("Invalid choice. Please select 0-71.")

        except ValueError as error:
            print("Input error:", error)

        except Exception as error:
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()
