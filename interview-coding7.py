"""coding interview problems in Python
1. Nth Fibonacci using Dynamic Programming
def fib(n):
    dp = [0]*(n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(10))  # Output: 55

2. Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')

3. Binary Search Tree (Insert, Search, Delete)
class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def minValueNode(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if not root: return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

4. Tree Traversals
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")

5. Height of Binary Tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

6. Graph (Adjacency List)
graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

7. BFS Traversal
from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            q.extend(graph[node])

bfs(graph, 'A')


8. DFS Traversal
def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neigh in graph[node]:
            dfs(graph, neigh, visited)

dfs(graph, 'A')

9. Dijkstra’s Algorithm
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]: continue
        for neigh, w in graph[node]:
            if d + w < dist[neigh]:
                dist[neigh] = d + w
                heapq.heappush(pq, (dist[neigh], neigh))
    return dist

graph = {
    'A': [('B',1),('C',4)],
    'B': [('C',2),('D',5)],
    'C': [('D',1)],
    'D': []
}
print(dijkstra(graph, 'A'))

10. N-Queens Problem
def solveNQueens(n):
    board = [["."]*n for _ in range(n)]
    res = []

    def isSafe(r,c):
        for i in range(r):
            if board[i][c] == "Q": return False
        for i,j in zip(range(r-1,-1,-1),range(c-1,-1,-1)):
            if board[i][j] == "Q": return False
        for i,j in zip(range(r-1,-1,-1),range(c+1,n)):
            if board[i][j] == "Q": return False
        return True

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if isSafe(r,c):
                board[r][c] = "Q"
                backtrack(r+1)
                board[r][c] = "."
    backtrack(0)
    return res

print(solveNQueens(4))
"""