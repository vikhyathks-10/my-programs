# 🔹 DAY 13 - ADVANCED ARRAY PROBLEMS


# ==================================================
# 🔹 1. Kadane's Algorithm
# ==================================================

def kadane_algorithm(arr):

    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):

        current_sum = max(arr[i],
                          current_sum + arr[i])

        max_sum = max(max_sum,
                      current_sum)

    return max_sum


# ==================================================
# 🔹 2. Stock Buy-Sell Profit
# ==================================================

def max_stock_profit(prices):

    min_price = prices[0]

    max_profit = 0

    for price in prices:

        min_price = min(min_price, price)

        profit = price - min_price

        max_profit = max(max_profit, profit)

    return max_profit


# ==================================================
# 🔹 3. Rainwater Trapping (Basic)
# ==================================================

def trap_rainwater(height):

    n = len(height)

    water = 0

    for i in range(1, n - 1):

        left_max = max(height[:i])

        right_max = max(height[i + 1:])

        water += max(
            min(left_max, right_max)
            - height[i],
            0
        )

    return water


# ==================================================
# 🔹 4. Container With Most Water
# ==================================================

def container_with_most_water(height):

    left = 0
    right = len(height) - 1

    max_area = 0

    while left < right:

        width = right - left

        area = min(
            height[left],
            height[right]
        ) * width

        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ==================================================
# 🔹 5. Peak Element Finder
# ==================================================

def peak_element(arr):

    n = len(arr)

    for i in range(n):

        left = arr[i - 1] if i > 0 else float('-inf')

        right = arr[i + 1] if i < n - 1 else float('-inf')

        if arr[i] > left and arr[i] > right:
            return arr[i]

    return -1


# ==================================================
# 🔹 MAIN PROGRAM
# ==================================================

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print("🔹 Kadane's Algorithm")
print(kadane_algorithm(arr))


print("\n🔹 Stock Buy-Sell Profit")

prices = [7, 1, 5, 3, 6, 4]

print(max_stock_profit(prices))


print("\n🔹 Rainwater Trapping")

height = [4, 2, 0, 3, 2, 5]

print(trap_rainwater(height))


print("\n🔹 Container With Most Water")

container = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(container_with_most_water(container))


print("\n🔹 Peak Element Finder")

peak_arr = [1, 3, 20, 4, 1, 0]

print(peak_element(peak_arr))