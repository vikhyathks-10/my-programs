# Graph using Adjacency List
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)   # undirected graph

# 1. BFS Traversal
    def bfs(self, start):
        visited = [False] * self.V
        q = deque([start])
        visited[start] = True

        print("BFS Traversal:", end=" ")
        while q:
            node = q.popleft()
            print(node, end=" ")
            for nbr in self.graph[node]:
                if not visited[nbr]:
                    visited[nbr] = True
                    q.append(nbr)
        print()

# 2. DFS Traversal (Recursive)
    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        for nbr in self.graph[node]:
            if not visited[nbr]:
                self.dfs_util(nbr, visited)

    def dfs(self, start):
        visited = [False] * self.V
        print("DFS Traversal:", end=" ")
        self.dfs_util(start, visited)
        print()

# 3. Detect Cycle in Undirected Graph
    def detect_cycle_util(self, v, visited, parent):
        visited[v] = True
        for nbr in self.graph[v]:
            if not visited[nbr]:
                if self.detect_cycle_util(nbr, visited, v):
                    return True
            elif parent != nbr:
                return True
        return False

    def detect_cycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.detect_cycle_util(i, visited, -1):
                    return True
        return False

# 4. Shortest Path using BFS
    def shortest_path(self, src):
        dist = [-1] * self.V
        q = deque([src])
        dist[src] = 0

        while q:
            node = q.popleft()
            for nbr in self.graph[node]:
                if dist[nbr] == -1:
                    dist[nbr] = dist[node] + 1
                    q.append(nbr)

        print("Shortest distance from", src, ":", dist)

# 5. Check if Graph is Connected
    def is_connected(self):
        visited = [False] * self.V
        self.dfs_util(0, visited)
        return all(visited)

# 6. Topological Sort (DFS) – Directed Graph
class DirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topo_util(self, v, visited, stack):
        visited[v] = True
        for nbr in self.graph[v]:
            if not visited[nbr]:
                self.topo_util(nbr, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topo_util(i, visited, stack)

        print("Topological Order:", stack[::-1])

# Testing
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

g.bfs(0)
g.dfs(0)
print("Cycle Exists:", g.detect_cycle())
g.shortest_path(0)
print("Graph Connected:", g.is_connected())

dg = DirectedGraph(6)
dg.add_edge(5, 2)
dg.add_edge(5, 0)
dg.add_edge(4, 0)
dg.add_edge(4, 1)
dg.add_edge(2, 3)
dg.add_edge(3, 1)
dg.topological_sort()
