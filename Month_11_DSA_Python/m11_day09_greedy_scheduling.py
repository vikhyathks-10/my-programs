
"""
MONTH 11 - DAY 9
GREEDY SCHEDULING PROBLEMS

Programs:
41. Minimum Railway Platforms
42. Meeting Rooms
43. Non-overlapping Intervals
44. Minimum Arrows to Burst Balloons
45. Maximum Length Chain of Pairs

Menu:
41-45: Run individual programs
46: Run all programs
0: Exit
"""


# ---------------------------------------------------------
# PROGRAM 41: MINIMUM NUMBER OF RAILWAY PLATFORMS
# ---------------------------------------------------------

def minimum_platforms(
    arrivals: list[int],
    departures: list[int]
) -> int:
    """
    Find the minimum number of railway platforms required.

    Each train's arrival and departure times are at the
    same index.

    If arrival and departure occur at the same time,
    they are considered to require separate platforms.
    """

    if len(arrivals) != len(departures):
        raise ValueError(
            "Arrivals and departures must have equal lengths."
        )

    if any(a > d for a, d in zip(arrivals, departures)):
        raise ValueError(
            "A train cannot depart before it arrives."
        )

    n = len(arrivals)

    if n == 0:
        return 0

    sorted_arrivals = sorted(arrivals)
    sorted_departures = sorted(departures)

    i = 0
    j = 0

    platforms_needed = 0
    maximum_platforms = 0

    while i < n:
        if sorted_arrivals[i] <= sorted_departures[j]:
            platforms_needed += 1
            maximum_platforms = max(
                maximum_platforms,
                platforms_needed
            )
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return maximum_platforms


def program_41() -> None:
    print("\nPROGRAM 41: MINIMUM RAILWAY PLATFORMS")

    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    print("Arrival times:", arrivals)
    print("Departure times:", departures)

    result = minimum_platforms(arrivals, departures)

    print("Minimum platforms required:", result)


# ---------------------------------------------------------
# PROGRAM 42: MEETING ROOMS
# ---------------------------------------------------------

def can_attend_all_meetings(
    meetings: list[tuple[int, int]]
) -> bool:
    """
    Return True if all meetings can be attended.

    A meeting ending at time t and another starting
    at time t do not overlap.
    """

    if any(start > end for start, end in meetings):
        raise ValueError("Meeting start cannot exceed end.")

    sorted_meetings = sorted(meetings)

    for i in range(1, len(sorted_meetings)):
        previous_end = sorted_meetings[i - 1][1]
        current_start = sorted_meetings[i][0]

        if current_start < previous_end:
            return False

    return True


def program_42() -> None:
    print("\nPROGRAM 42: MEETING ROOMS")

    meetings = [
        (0, 30),
        (5, 10),
        (15, 20)
    ]

    print("Meeting intervals:", meetings)

    result = can_attend_all_meetings(meetings)

    if result:
        print("All meetings can be attended.")
    else:
        print("All meetings cannot be attended.")


# ---------------------------------------------------------
# PROGRAM 43: NON-OVERLAPPING INTERVALS
# ---------------------------------------------------------

def erase_overlap_intervals(
    intervals: list[tuple[int, int]]
) -> tuple[int, list[tuple[int, int]]]:
    """
    Return the minimum number of intervals to remove
    and the intervals retained.

    Intervals touching at endpoints are compatible.
    """

    if any(start >= end for start, end in intervals):
        raise ValueError(
            "Each interval must have start < end."
        )

    sorted_intervals = sorted(
        intervals,
        key=lambda interval: interval[1]
    )

    kept: list[tuple[int, int]] = []
    last_end = float("-inf")

    for start, end in sorted_intervals:
        if start >= last_end:
            kept.append((start, end))
            last_end = end

    removed_count = len(intervals) - len(kept)

    return removed_count, kept


def program_43() -> None:
    print("\nPROGRAM 43: NON-OVERLAPPING INTERVALS")

    intervals = [
        (1, 2),
        (2, 3),
        (3, 4),
        (1, 3)
    ]

    print("Original intervals:", intervals)

    removed, kept = erase_overlap_intervals(intervals)

    print("Intervals retained:", kept)
    print("Minimum intervals to remove:", removed)


# ---------------------------------------------------------
# PROGRAM 44: MINIMUM ARROWS TO BURST BALLOONS
# ---------------------------------------------------------

def minimum_arrows(
    balloons: list[tuple[int, int]]
) -> tuple[int, list[int]]:
    """
    Find the minimum arrows needed to burst all balloons.

    Each balloon covers a closed interval [start, end].
    An arrow at x bursts every balloon containing x.
    """

    if any(start > end for start, end in balloons):
        raise ValueError(
            "Balloon start cannot exceed end."
        )

    if not balloons:
        return 0, []

    sorted_balloons = sorted(
        balloons,
        key=lambda balloon: balloon[1]
    )

    arrow_positions: list[int] = []

    for start, end in sorted_balloons:
        if not arrow_positions or start > arrow_positions[-1]:
            arrow_positions.append(end)

    return len(arrow_positions), arrow_positions


def program_44() -> None:
    print("\nPROGRAM 44: MINIMUM ARROWS TO BURST BALLOONS")

    balloons = [
        (10, 16),
        (2, 8),
        (1, 6),
        (7, 12)
    ]

    print("Balloon intervals:", balloons)

    count, positions = minimum_arrows(balloons)

    print("Arrow positions:", positions)
    print("Minimum arrows required:", count)


# ---------------------------------------------------------
# PROGRAM 45: MAXIMUM LENGTH CHAIN OF PAIRS
# ---------------------------------------------------------

def maximum_pair_chain(
    pairs: list[tuple[int, int]]
) -> tuple[int, list[tuple[int, int]]]:
    """
    Find the maximum length chain of pairs.

    A pair (a, b) can precede (c, d) only when b < c.
    """

    if any(a >= b for a, b in pairs):
        raise ValueError(
            "Each pair must satisfy first < second."
        )

    sorted_pairs = sorted(
        pairs,
        key=lambda pair: pair[1]
    )

    chain: list[tuple[int, int]] = []
    last_end = float("-inf")

    for first, second in sorted_pairs:
        if first > last_end:
            chain.append((first, second))
            last_end = second

    return len(chain), chain


def program_45() -> None:
    print("\nPROGRAM 45: MAXIMUM LENGTH CHAIN OF PAIRS")

    pairs = [
        (1, 2),
        (2, 3),
        (3, 4)
    ]

    print("Original pairs:", pairs)

    length, chain = maximum_pair_chain(pairs)

    print("Maximum chain:", chain)
    print("Maximum chain length:", length)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    while True:
        print("\n========================================")
        print(" MONTH 11 - DAY 9: GREEDY SCHEDULING")
        print("========================================")
        print("41. Minimum Railway Platforms")
        print("42. Meeting Rooms")
        print("43. Non-overlapping Intervals")
        print("44. Minimum Arrows to Burst Balloons")
        print("45. Maximum Length Chain of Pairs")
        print("46. Run All Programs")
        print("0. Exit")
        print("========================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 41:
            program_41()
        elif choice == 42:
            program_42()
        elif choice == 43:
            program_43()
        elif choice == 44:
            program_44()
        elif choice == 45:
            program_45()
        elif choice == 46:
            for program in (
                program_41,
                program_42,
                program_43,
                program_44,
                program_45
            ):
                program()
        elif choice == 0:
            print("Exiting Day 9 programs. Keep practicing!")
            break
        else:
            print("Invalid choice. Please select 0 or 41-46.")


if __name__ == "__main__":
    main()
