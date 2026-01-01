"""interview Coding Problems in Python

Solve Job Scheduling Problem (Max Profit with Deadlines)
def job_scheduling(jobs):
    # jobs = [(profit, deadline)]
    jobs.sort(key=lambda x: x[0], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slot = [False]*max_deadline
    profit = 0
    for p, d in jobs:
        for i in range(d-1, -1, -1):
            if not slot[i]:
                slot[i] = True
                profit += p
                break
    return profit

# Example
jobs = [(100,2),(19,1),(27,2),(25,1),(15,3)]
print(job_scheduling(jobs))  # Output: 142

Find Median of Two Sorted Arrays
def find_median_sorted_arrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)
    if n % 2 == 1:
        return nums[n//2]
    else:
        return (nums[n//2 - 1] + nums[n//2]) / 2

# Example
print(find_median_sorted_arrays([1,3],[2]))       # 2
print(find_median_sorted_arrays([1,2],[3,4]))     # 2.5

Check if a Sudoku Board is Valid
def is_valid_sudoku(board):
    for i in range(9):
        row = [x for x in board[i] if x != '.']
        if len(row) != len(set(row)):
            return False
        col = [board[x][i] for x in range(9) if board[x][i] != '.']
        if len(col) != len(set(col)):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = [board[x][y] for x in range(i,i+3) for y in range(j,j+3) if board[x][y] != '.']
            if len(block) != len(set(block)):
                return False
    return True

# Example
sudoku_board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(sudoku_board))  # True

Implement Conway’s Game of Life
def game_of_life(board):
    m, n = len(board), len(board[0])
    copy = [[board[i][j] for j in range(n)] for i in range(m)]
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for i in range(m):
        for j in range(n):
            live = sum(copy[i+x][j+y] == 1 for x,y in directions if 0<=i+x<m and 0<=j+y<n)
            if copy[i][j] == 1 and (live < 2 or live > 3):
                board[i][j] = 0
            if copy[i][j] == 0 and live == 3:
                board[i][j] = 1
    return board

# Example
board = [
 [0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]
]
print(game_of_life(board))

Design a Simple Chatbot (Rule-Based)
def chatbot():
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day!"
    }
    print("Chatbot (type 'bye' to exit)")
    while True:
        msg = input("You: ").lower()
        if msg == 'bye':
            print("Bot:", responses["bye"])
            break
        response = responses.get(msg, "Sorry, I didn't understand that.")
        print("Bot:", response)

# Example usage
# chatbot()
"""
"""
Find All Subsets of a Set (Power Set)
def subsets(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result

# Example
print(subsets([1,2,3]))
# Output: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Find the Maximum Subarray Sum (Kadane’s Algorithm)
def max_subarray(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

# Example
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

Merge Intervals
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

# Example
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]]

Find All Permutations of a String
def permute(s):
    if len(s) == 0:
        return ['']
    smaller = permute(s[1:])
    return [s[0]+p for p in smaller] + [p+s[0] for p in smaller if s[0] not in p]

# Example
print(permute("abc"))
# Output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

Rotate a Matrix 90 Degrees Clockwise
def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # transpose
    for i in range(n):
        matrix[i].reverse()  # reverse rows
    return matrix

# Example
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(rotate_matrix(matrix))
# Output: [[7,4,1],[8,5,2],[9,6,3]]

"""