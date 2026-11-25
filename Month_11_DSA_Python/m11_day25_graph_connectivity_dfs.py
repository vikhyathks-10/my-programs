
from collections import defaultdict


# ============================================================
# PROGRAM 121: TARJAN'S ALGORITHM
# Find Strongly Connected Components in a directed graph.
# ============================================================

def tarjan_scc(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[list[int]]:

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:
        graph[u].append(v)

    discovery = [-1] * vertices
    low = [0] * vertices
    on_stack = [False] * vertices

    stack: list[int] = []
    components: list[list[int]] = []

    timer = 0

    def dfs(node: int) -> None:
        nonlocal timer

        discovery[node] = timer
        low[node] = timer
        timer += 1

        stack.append(node)
        on_stack[node] = True

        for neighbour in graph[node]:

            if discovery[neighbour] == -1:
                dfs(neighbour)
                low[node] = min(low[node], low[neighbour])

            elif on_stack[neighbour]:
                low[node] = min(low[node], discovery[neighbour])

        # If node is the root of an SCC, pop the SCC.
        if low[node] == discovery[node]:
            component: list[int] = []

            while True:
                current = stack.pop()
                on_stack[current] = False
                component.append(current)

                if current == node:
                    break

            components.append(sorted(component))

    # Handle disconnected portions of the directed graph.
    for vertex in range(vertices):
        if discovery[vertex] == -1:
            dfs(vertex)

    return components


def demo_121() -> None:
    vertices = 5

    edges = [
        (0, 2),
        (2, 1),
        (1, 0),
        (0, 3),
        (3, 4)
    ]

    print("Vertices:", vertices)
    print("Directed Edges:", edges)

    components = tarjan_scc(vertices, edges)

    print("\nStrongly Connected Components:")

    for index, component in enumerate(components, start=1):
        print(f"SCC {index}: {component}")


# ============================================================
# PROGRAM 122: FIND MOTHER VERTEX
# Find a vertex from which all other vertices are reachable.
# ============================================================

def find_mother_vertex(
    vertices: int,
    edges: list[tuple[int, int]]
) -> int:

    if vertices == 0:
        return -1

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:
        graph[u].append(v)

    visited = [False] * vertices
    candidate = -1

    # First DFS: Find the last-finished candidate.
    def dfs(node: int) -> None:
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)

    for vertex in range(vertices):
        if not visited[vertex]:
            dfs(vertex)
            candidate = vertex

    # Second DFS: Verify that the candidate reaches all vertices.
    visited = [False] * vertices
    dfs(candidate)

    if all(visited):
        return candidate

    return -1


def demo_122() -> None:
    vertices = 5

    edges = [
        (0, 1),
        (0, 2),
        (2, 3),
        (3, 4),
        (4, 0)
    ]

    print("Vertices:", vertices)
    print("Directed Edges:", edges)

    result = find_mother_vertex(vertices, edges)

    if result == -1:
        print("\nNo Mother Vertex exists.")
    else:
        print("\nMother Vertex:", result)


# ============================================================
# PROGRAM 123: CRITICAL CONNECTIONS IN A NETWORK
# Find all bridges in an undirected graph.
# Uses Tarjan's bridge-finding algorithm.
# ============================================================

def critical_connections(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[tuple[int, int]]:

    # Store neighbour and edge ID.
    # Edge IDs also handle parallel edges correctly.
    graph: list[list[tuple[int, int]]] = [
        [] for _ in range(vertices)
    ]

    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))

    discovery = [-1] * vertices
    low = [0] * vertices

    timer = 0
    bridges: list[tuple[int, int]] = []

    def dfs(node: int, parent_edge: int) -> None:
        nonlocal timer

        discovery[node] = timer
        low[node] = timer
        timer += 1

        for neighbour, edge_id in graph[node]:

            # Skip the exact edge used to enter this node.
            if edge_id == parent_edge:
                continue

            if discovery[neighbour] == -1:
                dfs(neighbour, edge_id)

                low[node] = min(low[node], low[neighbour])

                if low[neighbour] > discovery[node]:
                    bridges.append(
                        (min(node, neighbour), max(node, neighbour))
                    )

            else:
                low[node] = min(
                    low[node],
                    discovery[neighbour]
                )

    # Handle disconnected graphs.
    for vertex in range(vertices):
        if discovery[vertex] == -1:
            dfs(vertex, -1)

    return sorted(bridges)


def demo_123() -> None:
    vertices = 5

    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (1, 3),
        (3, 4)
    ]

    print("Vertices:", vertices)
    print("Connections:", edges)

    print(
        "\nCritical Connections:",
        critical_connections(vertices, edges)
    )


# ============================================================
# PROGRAM 124: NUMBER OF OPERATIONS TO MAKE NETWORK CONNECTED
# Find minimum cable rearrangements to connect all computers.
# ============================================================

def make_connected(
    computers: int,
    connections: list[tuple[int, int]]
) -> int:

    if computers <= 1:
        return 0

    # At least computers - 1 cables are required.
    if len(connections) < computers - 1:
        return -1

    graph: list[list[int]] = [[] for _ in range(computers)]

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * computers
    components = 0

    def dfs(node: int) -> None:
        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)

    # Count connected components.
    for computer in range(computers):
        if not visited[computer]:
            components += 1
            dfs(computer)

    # One operation can connect two components.
    return components - 1


def demo_124() -> None:
    computers = 6

    connections = [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3)
    ]

    print("Number of Computers:", computers)
    print("Connections:", connections)

    result = make_connected(computers, connections)

    print("\nMinimum Operations Required:", result)


# ============================================================
# PROGRAM 125: ACCOUNTS MERGE
# Merge accounts that share at least one email address.
# Uses Disjoint Set Union (DSU).
# ============================================================

class DisjointSet:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}
        self.rank: dict[str, int] = {}

    def add(self, value: str) -> None:
        if value not in self.parent:
            self.parent[value] = value
            self.rank[value] = 0

    def find(self, value: str) -> str:
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])

        return self.parent[value]

    def union(self, first: str, second: str) -> None:
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return

        if self.rank[root_first] < self.rank[root_second]:
            self.parent[root_first] = root_second

        elif self.rank[root_first] > self.rank[root_second]:
            self.parent[root_second] = root_first

        else:
            self.parent[root_second] = root_first
            self.rank[root_first] += 1


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    dsu = DisjointSet()

    # Map each email to the account owner's name.
    email_to_name: dict[str, str] = {}

    for account in accounts:
        name = account[0]
        emails = account[1:]

        for email in emails:
            dsu.add(email)
            email_to_name[email] = name

        # Connect every email in this account.
        if emails:
            first_email = emails[0]

            for email in emails[1:]:
                dsu.union(first_email, email)

    # Group emails by their DSU representative.
    merged_emails: dict[str, list[str]] = defaultdict(list)

    for email in dsu.parent:
        root = dsu.find(email)
        merged_emails[root].append(email)

    result: list[list[str]] = []

    for root, emails in merged_emails.items():
        emails.sort()

        name = email_to_name[root]
        result.append([name] + emails)

    # Sort output for consistent display.
    result.sort(key=lambda account: (account[0], account[1:]))

    return result


def demo_125() -> None:
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]

    print("Original Accounts:")

    for account in accounts:
        print(account)

    merged = accounts_merge(accounts)

    print("\nMerged Accounts:")

    for account in merged:
        print(account)


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    programs = {
        121: demo_121,
        122: demo_122,
        123: demo_123,
        124: demo_124,
        125: demo_125
    }

    while True:
        print("\n" + "=" * 60)
        print("MONTH 11 - DAY 25: GRAPH CONNECTIVITY AND DFS")
        print("=" * 60)

        print("121. Tarjan's Algorithm - Strongly Connected Components")
        print("122. Find Mother Vertex")
        print("123. Critical Connections in a Network")
        print("124. Make Network Connected")
        print("125. Accounts Merge")
        print("126. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Day 25 completed. Keep practicing!")
            break

        elif choice == 126:
            for number in range(121, 126):
                print("\n" + "#" * 60)
                print(f"RUNNING PROGRAM {number}")
                print("#" * 60)
                programs[number]()

        elif choice in programs:
            programs[choice]()

        else:
            print("Invalid choice. Please select 121–126 or 0.")


if __name__ == "__main__":
    main()
