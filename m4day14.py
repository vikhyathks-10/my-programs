# 🔹 DAY 14 - MIXED RECURSION PRACTICE


# 🔹 1. Reverse an Array (Recursion)
def reverse_array(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start+1, end-1)


# 🔹 2. Check if String is Palindrome (Recursion)
def is_palindrome_str(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palindrome_str(s, start+1, end-1)


# 🔹 3. Find All Indices of Element
def find_all_indices(arr, index, target, result):
    if index == len(arr):
        return
    if arr[index] == target:
        result.append(index)
    find_all_indices(arr, index+1, target, result)


# 🔹 4. Generate All Binary Strings of Length N
def generate_binary(n, current=""):
    if len(current) == n:
        print(current)
        return
    generate_binary(n, current + "0")
    generate_binary(n, current + "1")


# 🔹 5. Count Paths with Obstacles (Maze)
def maze_with_obstacles(grid, i, j):
    if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 1:
        return 0
    if i == len(grid)-1 and j == len(grid[0])-1:
        return 1
    return (maze_with_obstacles(grid, i+1, j) +
            maze_with_obstacles(grid, i, j+1))


# 🔹 MAIN PROGRAM

print("\n--- Reverse Array ---")
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr)-1)
print(arr)


print("\n--- String Palindrome ---")
s = "madam"
print("Is Palindrome:", is_palindrome_str(s, 0, len(s)-1))


print("\n--- Find All Indices ---")
arr = [1, 2, 3, 2, 4, 2]
result = []
find_all_indices(arr, 0, 2, result)
print("Indices:", result)


print("\n--- Binary Strings ---")
generate_binary(3)


print("\n--- Maze with Obstacles ---")
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print("Paths:", maze_with_obstacles(grid, 0, 0))