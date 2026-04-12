# 🔹 DAY 12 - ADVANCED RECURSION


# 🔹 1. Tower of Hanoi
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, helper, source, destination)


# 🔹 2. Maze Path Count (Right & Down only)
def maze_paths(i, j, n, m):
    if i == n-1 and j == m-1:
        return 1
    if i >= n or j >= m:
        return 0
    return maze_paths(i+1, j, n, m) + maze_paths(i, j+1, n, m)


# 🔹 3. Climbing Stairs
def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    return climb_stairs(n-1) + climb_stairs(n-2)


# 🔹 4. Subset Sum (Check if subset equals target)
def subset_sum(arr, index, target):
    if target == 0:
        return True
    if index == len(arr) or target < 0:
        return False

    # include or exclude
    return (subset_sum(arr, index+1, target-arr[index]) or
            subset_sum(arr, index+1, target))


# 🔹 5. Combination Generation
def combinations(arr, index, current):
    if index == len(arr):
        print(current)
        return

    # include
    combinations(arr, index+1, current + [arr[index]])

    # exclude
    combinations(arr, index+1, current)


# 🔹 MAIN PROGRAM

print("\n--- Tower of Hanoi ---")
tower_of_hanoi(3, 'A', 'B', 'C')


print("\n--- Maze Path Count ---")
print("Paths in 3x3 grid:", maze_paths(0, 0, 3, 3))


print("\n--- Climbing Stairs ---")
print("Ways to climb 5 steps:", climb_stairs(5))


print("\n--- Subset Sum ---")
arr = [2, 4, 6, 8]
target = 10
print("Subset sum exists:", subset_sum(arr, 0, target))


print("\n--- Combinations ---")
combinations([1, 2, 3], 0, [])