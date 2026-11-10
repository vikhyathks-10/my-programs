
"""
MONTH 11 - DAY 10
ADVANCED GREEDY PROBLEMS

Programs:
46. Jump Game
47. Jump Game II
48. Gas Station
49. Candy Distribution
50. Partition Labels

Menu:
46-50: Run individual programs
51: Run all programs
0: Exit
"""

from typing import Optional


# ---------------------------------------------------------
# PROGRAM 46: JUMP GAME
# ---------------------------------------------------------

def can_reach_last_index(nums: list[int]) -> bool:
    """
    Determine whether the last index is reachable.

    nums[i] represents the maximum jump length
    from index i.
    """

    if not nums:
        return False

    if any(value < 0 for value in nums):
        raise ValueError("Jump lengths cannot be negative.")

    farthest = 0

    for index, jump in enumerate(nums):

        # Current index cannot be reached.
        if index > farthest:
            return False

        farthest = max(farthest, index + jump)

        # Last index is reachable.
        if farthest >= len(nums) - 1:
            return True

    return True


def program_46() -> None:
    print("\nPROGRAM 46: JUMP GAME")

    nums = [2, 3, 1, 1, 4]

    print("Jump array:", nums)

    result = can_reach_last_index(nums)

    if result:
        print("The last index is reachable.")
    else:
        print("The last index is not reachable.")


# ---------------------------------------------------------
# PROGRAM 47: JUMP GAME II
# ---------------------------------------------------------

def minimum_jumps(nums: list[int]) -> Optional[int]:
    """
    Find the minimum number of jumps required to reach
    the last index.

    Returns None if the last index is unreachable.
    """

    if not nums:
        return None

    if any(value < 0 for value in nums):
        raise ValueError("Jump lengths cannot be negative.")

    if len(nums) == 1:
        return 0

    jumps = 0
    current_end = 0
    farthest = 0

    for index in range(len(nums) - 1):

        # This position cannot be reached.
        if index > farthest:
            return None

        farthest = max(farthest, index + nums[index])

        # We have reached the end of the current jump range.
        if index == current_end:
            # No progress is possible.
            if farthest == current_end:
                return None

            jumps += 1
            current_end = farthest

            if current_end >= len(nums) - 1:
                return jumps

    return None


def program_47() -> None:
    print("\nPROGRAM 47: JUMP GAME II")

    nums = [2, 3, 1, 1, 4]

    print("Jump array:", nums)

    result = minimum_jumps(nums)

    if result is not None:
        print("Minimum jumps required:", result)
    else:
        print("The last index cannot be reached.")


# ---------------------------------------------------------
# PROGRAM 48: GAS STATION
# ---------------------------------------------------------

def gas_station_start(
    gas: list[int],
    cost: list[int]
) -> int:
    """
    Find the starting station from which a complete
    circular journey is possible.

    Returns -1 if no valid starting station exists.
    """

    if len(gas) != len(cost):
        raise ValueError(
            "Gas and cost arrays must have equal lengths."
        )

    if any(value < 0 for value in gas + cost):
        raise ValueError("Gas and cost values cannot be negative.")

    if not gas:
        return -1

    total_gas = 0
    current_gas = 0
    start = 0

    for index in range(len(gas)):
        difference = gas[index] - cost[index]

        total_gas += difference
        current_gas += difference

        # This starting point cannot complete the journey.
        if current_gas < 0:
            start = index + 1
            current_gas = 0

    if total_gas >= 0 and start < len(gas):
        return start

    return -1


def program_48() -> None:
    print("\nPROGRAM 48: GAS STATION")

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]

    print("Gas available:", gas)
    print("Travel cost:", cost)

    result = gas_station_start(gas, cost)

    if result != -1:
        print("Valid starting station index:", result)
        print("Starting station number:", result + 1)
    else:
        print("No valid starting station exists.")


# ---------------------------------------------------------
# PROGRAM 49: CANDY DISTRIBUTION
# ---------------------------------------------------------

def minimum_candies(ratings: list[int]) -> tuple[int, list[int]]:
    """
    Distribute candies such that:
    1. Every child receives at least one candy.
    2. A child with a higher rating than an adjacent
       child receives more candies.

    Return the minimum total and the distribution.
    """

    n = len(ratings)

    if n == 0:
        return 0, []

    candies = [1] * n

    # Left-to-right pass.
    for index in range(1, n):
        if ratings[index] > ratings[index - 1]:
            candies[index] = candies[index - 1] + 1

    # Right-to-left pass.
    for index in range(n - 2, -1, -1):
        if ratings[index] > ratings[index + 1]:
            candies[index] = max(
                candies[index],
                candies[index + 1] + 1
            )

    return sum(candies), candies


def program_49() -> None:
    print("\nPROGRAM 49: CANDY DISTRIBUTION")

    ratings = [1, 0, 2]

    print("Children's ratings:", ratings)

    total, distribution = minimum_candies(ratings)

    print("Candy distribution:", distribution)
    print("Minimum candies required:", total)


# ---------------------------------------------------------
# PROGRAM 50: PARTITION LABELS
# ---------------------------------------------------------

def partition_labels(text: str) -> list[int]:
    """
    Divide a string into the maximum number of partitions
    such that each character appears in at most one partition.

    Return the length of each partition.
    """

    if not text:
        return []

    # Store the last occurrence of every character.
    last_position: dict[str, int] = {}

    for index, character in enumerate(text):
        last_position[character] = index

    result: list[int] = []

    start = 0
    end = 0

    for index, character in enumerate(text):

        # Extend the current partition to include
        # the last occurrence of this character.
        end = max(end, last_position[character])

        # A partition is complete when every character
        # inside it has its last occurrence within it.
        if index == end:
            result.append(end - start + 1)
            start = index + 1

    return result


def program_50() -> None:
    print("\nPROGRAM 50: PARTITION LABELS")

    text = "ababcbacadefegdehijhklij"

    print("Original string:", text)

    result = partition_labels(text)

    print("Partition lengths:", result)
    print("Number of partitions:", len(result))


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 10: ADVANCED GREEDY")
        print("========================================")
        print("46. Jump Game")
        print("47. Jump Game II")
        print("48. Gas Station")
        print("49. Candy Distribution")
        print("50. Partition Labels")
        print("51. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 46:
            program_46()
        elif choice == 47:
            program_47()
        elif choice == 48:
            program_48()
        elif choice == 49:
            program_49()
        elif choice == 50:
            program_50()
        elif choice == 51:
            for program in (
                program_46,
                program_47,
                program_48,
                program_49,
                program_50
            ):
                program()
        elif choice == 0:
            print("Exiting Day 10 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 46-51.")


if __name__ == "__main__":
    main()
