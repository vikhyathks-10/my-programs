
# MONTH 10 - DAY 10
# Monotonic Stack Problems
# Programs 46-50

from __future__ import annotations


# ---------------------------------------------------------
# ARRAY INPUT
# ---------------------------------------------------------
def get_array(prompt: str = "Enter array elements: ") -> list[int]:
    text = input(prompt).strip()

    if not text:
        return []

    return list(map(int, text.split()))


# =========================================================
# PROGRAM 46
# NEXT GREATER ELEMENT TO THE RIGHT
# =========================================================
def next_greater_right(arr: list[int]) -> list[int | None]:
    n = len(arr)
    result: list[int | None] = [None] * n
    stack: list[int] = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


def program_46() -> None:
    arr = get_array()
    result = next_greater_right(arr)

    print("Array:", arr)
    print("Next greater element to the right:", result)


# =========================================================
# PROGRAM 47
# NEXT SMALLER ELEMENT TO THE RIGHT
# =========================================================
def next_smaller_right(arr: list[int]) -> list[int | None]:
    n = len(arr)
    result: list[int | None] = [None] * n
    stack: list[int] = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


def program_47() -> None:
    arr = get_array()
    result = next_smaller_right(arr)

    print("Array:", arr)
    print("Next smaller element to the right:", result)


# =========================================================
# PROGRAM 48
# PREVIOUS GREATER ELEMENT
# =========================================================
def previous_greater(arr: list[int]) -> list[int | None]:
    result: list[int | None] = []
    stack: list[int] = []

    for value in arr:
        while stack and stack[-1] <= value:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(None)

        stack.append(value)

    return result


def program_48() -> None:
    arr = get_array()
    result = previous_greater(arr)

    print("Array:", arr)
    print("Previous greater element:", result)


# =========================================================
# PROGRAM 49
# STOCK SPAN PROBLEM
# =========================================================
def stock_span(prices: list[int]) -> list[int]:
    spans: list[int] = []
    stack: list[int] = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] <= price:
            stack.pop()

        if not stack:
            span = i + 1
        else:
            span = i - stack[-1]

        spans.append(span)
        stack.append(i)

    return spans


def program_49() -> None:
    prices = get_array("Enter daily stock prices: ")
    result = stock_span(prices)

    print("Stock prices:", prices)
    print("Stock spans:", result)


# =========================================================
# PROGRAM 50
# LARGEST RECTANGLE IN A HISTOGRAM
# =========================================================
def largest_rectangle(heights: list[int]) -> int:
    if any(height < 0 for height in heights):
        raise ValueError("Histogram heights cannot be negative.")

    stack: list[int] = []
    max_area = 0
    n = len(heights)

    # The extra iteration uses height 0 to process remaining bars.
    for i in range(n + 1):
        current_height = heights[i] if i < n else 0

        while stack and heights[stack[-1]] > current_height:
            height = heights[stack.pop()]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            max_area = max(max_area, height * width)

        if i < n:
            stack.append(i)

    return max_area


def program_50() -> None:
    heights = get_array("Enter histogram bar heights: ")
    area = largest_rectangle(heights)

    print("Histogram heights:", heights)
    print("Largest rectangle area:", area)


# =========================================================
# MAIN MENU
# =========================================================
def main() -> None:
    while True:
        print("\n======================================")
        print(" MONTH 10 - DAY 10")
        print(" MONOTONIC STACK PROBLEMS")
        print("======================================")
        print("46. Next greater element to the right")
        print("47. Next smaller element to the right")
        print("48. Previous greater element")
        print("49. Stock span problem")
        print("50. Largest rectangle in a histogram")
        print("51. Run all programs")
        print("52. Exit")
        print("======================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue

        try:
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
                print("\nProgram 46: Next Greater Element")
                program_46()

                print("\nProgram 47: Next Smaller Element")
                program_47()

                print("\nProgram 48: Previous Greater Element")
                program_48()

                print("\nProgram 49: Stock Span")
                program_49()

                print("\nProgram 50: Largest Histogram Rectangle")
                program_50()

            elif choice == 52:
                print("Exiting Month 10 - Day 10. Keep practicing!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    main()

