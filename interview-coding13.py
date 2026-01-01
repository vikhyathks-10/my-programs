"""interview Coding Problems 1-100 in Python

Find Edit Distance (Levenshtein Distance)

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# Example
print(edit_distance("kitten", "sitting"))  # Output: 3

Solve Word Break Problem Using DP

def word_break(s, word_dict):
    n = len(s)
    dp = [False]*(n+1)
    dp[0] = True
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]

# Example
word_dict = {"leet", "code"}
print(word_break("leetcode", word_dict))  # True

Solve Rat in a Maze Problem (Backtracking)

def rat_in_maze(maze):
    n = len(maze)
    path = []

    def solve(x, y):
        if x == y == n-1:
            path.append((x,y))
            return True
        if 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
            path.append((x,y))
            maze[x][y] = -1
            if solve(x+1, y) or solve(x, y+1):
                return True
            path.pop()
            maze[x][y] = 1
        return False

    if solve(0,0):
        return path
    return None

# Example
maze = [[1,0,0,0],
        [1,1,0,1],
        [0,1,0,0],
        [1,1,1,1]]
print(rat_in_maze(maze))

Count Number of Paths in a Grid (DP)

def count_paths(m, n):
    dp = [[1]*n for _ in range(m)]  # first row and column = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# Example
print(count_paths(3, 3))  # Output: 6

Count Number of Ways to Climb n Stairs (DP)

def climb_stairs(n):
    if n <= 1: return 1
    dp = [0]*(n+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]  # can climb 1 or 2 steps
    return dp[n]

# Example
print(climb_stairs(5))  # Output: 8

Implement LRU Cache

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)      # Evicts key 2
print(lru.get(2))  # -1

Implement a Hash Table

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

# Example
ht = HashTable()
ht.set("name", "Alice")
ht.set("age", 25)
print(ht.get("name"))  # Alice
print(ht.get("age"))   # 25

Design a Basic Calculator (String Expression Evaluation)

def calculate(s):
    stack, num, sign = [], 0, '+'
    s += '+'
    for c in s:
        if c.isdigit():
            num = num*10 + int(c)
        elif c in '+-*/':
            if sign == '+': stack.append(num)
            elif sign == '-': stack.append(-num)
            elif sign == '*': stack.append(stack.pop()*num)
            elif sign == '/': stack.append(int(stack.pop()/num))
            num, sign = 0, c
    return sum(stack)
# Example
print(calculate("3+2*2"))  # 7
print(calculate(" 3/2 "))  # 1
print(calculate(" 3+5 / 2 "))  # 5

Implement Topological Sorting of a Graph

from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    return stack[::-1]
# Example
graph = defaultdict(list)
graph[5] = [2,0]
graph[4] = [0,1]
graph[2] = [3]
graph[3] = [1]
graph[0] = []
graph[1] = []
print(topological_sort(graph))  # Output: [4,5,2,3,1,0] (one valid topo sort)

Detect Deadlock in a Resource Allocation Graph

def is_deadlock(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False
# Example
graph = { 'P1':['R1'], 'R1':['P2'], 'P2':['R2'], 'R2':['P1'] }  # Cycle
print(is_deadlock(graph))  # True
"""
