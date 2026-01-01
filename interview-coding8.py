"""interview-coding

11. Sudoku Solver (Backtracking)
def solveSudoku(board):
    def isValid(r,c,ch):
        for i in range(9):
            if board[i][c] == ch or board[r][i] == ch: return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch: return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for ch in "123456789":
                        if isValid(i,j,ch):
                            board[i][j] = ch
                            if backtrack(): return True
                            board[i][j] = "."
                    return False
        return True
    backtrack()

12. Longest Palindrome Substring
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # Odd length
        l,r = i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1) > len(res): res = s[l:r+1]
            l-=1; r+=1
        # Even length
        l,r = i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1) > len(res): res = s[l:r+1]
            l-=1; r+=1
    return res
print(longestPalindrome("babad"))

13. All Subsets of a Set
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res

print(subsets([1,2,3]))

14. Permutations of a String
def permute(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        ch = s[i]
        ros = s[:i] + s[i+1:]
        permute(ros, ans+ch)

permute("ABC")

15. Knapsack Problem (0/1 DP)
def knapsack(W, wt, val, n):
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0: dp[i][w]=0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

print(knapsack(50,[10,20,30],[60,100,120],3))

16. Coin Change Problem
def coinChange(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for c in coins:
        for i in range(c, amount+1):
            dp[i] = min(dp[i], 1+dp[i-c])
    return dp[amount] if dp[amount]!=float('inf') else -1

print(coinChange([1,2,5], 11))  # Output: 3

17. Maximum Subarray Sum (Kadane’s Algorithm)
def maxSubArray(nums):
    max_sum = nums[0]
    curr = 0
    for n in nums:
        curr = max(n, curr+n)
        max_sum = max(max_sum, curr)
    return max_sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

18. Detect Cycle in Graph
def isCyclic(graph):
    visited = set()
    recStack = set()

    def dfs(v):
        visited.add(v)
        recStack.add(v)
        for neigh in graph[v]:
            if neigh not in visited and dfs(neigh):
                return True
            elif neigh in recStack:
                return True
        recStack.remove(v)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node): return True
    return False

graph = {0:[1],1:[2],2:[0]}
print(isCyclic(graph))  # True

19. Check if Binary Tree is Balanced
def isBalanced(root):
    def dfs(node):
        if not node: return (0, True)
        lh, lb = dfs(node.left)
        rh, rb = dfs(node.right)
        return (1+max(lh,rh), lb and rb and abs(lh-rh)<=1)
    return dfs(root)[1]

def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    visited=set()

    def dfs(r,c):
        if (r<0 or c<0 or r>=rows or c>=cols or 
            grid[r][c]=='0' or (r,c) in visited): return
        visited.add((r,c))
        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)

    count=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]=='1' and (r,c) not in visited:
                dfs(r,c)
                count+=1
    return count
grid = [
 ["1","1","0","0"],
 ["1","0","0","1"],
 ["0","0","1","1"]
]
print(numIslands(grid))  # Output: 3
"""