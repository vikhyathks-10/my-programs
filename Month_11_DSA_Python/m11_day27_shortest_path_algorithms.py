
import heapq
from typing import Optional


# ---------------------------------------------------------
# PROGRAM 131: DIJKSTRA'S ALGORITHM
# ---------------------------------------------------------

def dijkstra(
    vertices: int,
    edges: list[tuple[int, int, int]],
    source: int
) -> list[float]:
    """
    Find shortest distances from source in a directed,
    weighted graph with non-negative edge weights.

    Each edge is (u, v, weight).
    """

    if vertices <= 0 or not 0 <= source < vertices:
        raise ValueError("Invalid number of vertices or source.")

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(vertices)
    ]

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")
        if weight < 0:
            raise ValueError("Dijkstra does not support negative weights.")

        adjacency[u].append((v, weight))

    distances: list[float] = [float("inf")] * vertices
    distances[source] = 0

    min_heap: list[tuple[float, int]] = [(0, source)]

    while min_heap:
        current_distance, node = heapq.heappop(min_heap)

        if current_distance > distances[node]:
            continue

        for neighbour, weight in adjacency[node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(
                    min_heap,
                    (new_distance, neighbour)
                )

    return distances


def run_131() -> None:
    print("\nPROGRAM 131: DIJKSTRA'S ALGORITHM")

    vertices = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
        (3, 4, 3)
    ]

    source = 0
    distances = dijkstra(vertices, edges, source)

    print("Source vertex:", source)
    print("Shortest distances:")

    for vertex, distance in enumerate(distances):
        print(f"Vertex {vertex}: {distance}")


# ---------------------------------------------------------
# PROGRAM 132: BELLMAN-FORD ALGORITHM
# ---------------------------------------------------------

def bellman_ford(
    vertices: int,
    edges: list[tuple[int, int, int]],
    source: int
) -> Optional[list[float]]:
    """
    Find shortest distances with possible negative edges.

    Returns None if a negative cycle is reachable
    from the source.
    """

    if vertices <= 0 or not 0 <= source < vertices:
        raise ValueError("Invalid number of vertices or source.")

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

    distances: list[float] = [float("inf")] * vertices
    distances[source] = 0

    # Relax all edges at most V - 1 times.
    for _ in range(vertices - 1):
        updated = False

        for u, v, weight in edges:
            if distances[u] != float("inf"):
                new_distance = distances[u] + weight

                if new_distance < distances[v]:
                    distances[v] = new_distance
                    updated = True

        if not updated:
            break

    # One more pass detects a reachable negative cycle.
    for u, v, weight in edges:
        if distances[u] != float("inf"):
            if distances[u] + weight < distances[v]:
                return None

    return distances


def run_132() -> None:
    print("\nPROGRAM 132: BELLMAN-FORD ALGORITHM")

    vertices = 5
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 3, 7)
    ]

    source = 0
    distances = bellman_ford(vertices, edges, source)

    if distances is None:
        print("Reachable negative-weight cycle detected.")
    else:
        print("Source vertex:", source)
        print("Shortest distances:")

        for vertex, distance in enumerate(distances):
            print(f"Vertex {vertex}: {distance}")

    print("\nNegative cycle test:")

    cycle_edges = [
        (0, 1, 1),
        (1, 2, -1),
        (2, 1, -1)
    ]

    cycle_result = bellman_ford(3, cycle_edges, 0)

    if cycle_result is None:
        print("Reachable negative-weight cycle detected.")
    else:
        print("No reachable negative-weight cycle.")


# ---------------------------------------------------------
# PROGRAM 133: FLOYD-WARSHALL ALGORITHM
# ---------------------------------------------------------

def floyd_warshall(
    vertices: int,
    edges: list[tuple[int, int, int]]
) -> list[list[float]]:
    """
    Find shortest distances between every pair of vertices.

    Each edge is (u, v, weight).
    This implementation treats the graph as directed.
    """

    if vertices <= 0:
        raise ValueError("Number of vertices must be positive.")

    distances: list[list[float]] = [
        [float("inf")] * vertices for _ in range(vertices)
    ]

    for vertex in range(vertices):
        distances[vertex][vertex] = 0

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

        distances[u][v] = min(distances[u][v], weight)

    # Consider every vertex as an intermediate vertex.
    for intermediate in range(vertices):
        for source in range(vertices):
            for destination in range(vertices):
                if (
                    distances[source][intermediate] != float("inf")
                    and distances[intermediate][destination] != float("inf")
                ):
                    new_distance = (
                        distances[source][intermediate]
                        + distances[intermediate][destination]
                    )

                    if new_distance < distances[source][destination]:
                        distances[source][destination] = new_distance

    return distances


def run_133() -> None:
    print("\nPROGRAM 133: FLOYD-WARSHALL ALGORITHM")

    vertices = 4
    edges = [
        (0, 1, 5),
        (0, 3, 10),
        (1, 2, 3),
        (2, 3, 1),
        (3, 0, 2)
    ]

    distances = floyd_warshall(vertices, edges)

    print("All-pairs shortest distance matrix:")

    for row in distances:
        print([
            "INF" if value == float("inf") else value
            for value in row
        ])

    # A negative diagonal value indicates a negative cycle.
    has_negative_cycle = any(
        distances[i][i] < 0 for i in range(vertices)
    )

    print("Negative cycle:", has_negative_cycle)


# ---------------------------------------------------------
# PROGRAM 134: SHORTEST PATH IN A DIRECTED ACYCLIC GRAPH
# ---------------------------------------------------------

def dag_shortest_path(
    vertices: int,
    edges: list[tuple[int, int, int]],
    source: int
) -> Optional[list[float]]:
    """
    Find shortest distances in a weighted DAG.

    Returns None if the graph contains a directed cycle.
    """

    if vertices <= 0 or not 0 <= source < vertices:
        raise ValueError("Invalid number of vertices or source.")

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(vertices)
    ]
    indegree = [0] * vertices

    for u, v, weight in edges:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Edge contains an invalid vertex.")

        adjacency[u].append((v, weight))
        indegree[v] += 1

    # Kahn's algorithm to generate topological order.
    queue: list[int] = [
        vertex
        for vertex in range(vertices)
        if indegree[vertex] == 0
    ]

    topological_order: list[int] = []
    front = 0

    while front < len(queue):
        node = queue[front]
        front += 1

        topological_order.append(node)

        for neighbour, _ in adjacency[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(topological_order) != vertices:
        return None

    distances: list[float] = [float("inf")] * vertices
    distances[source] = 0

    # Relax edges in topological order.
    for node in topological_order:
        if distances[node] == float("inf"):
            continue

        for neighbour, weight in adjacency[node]:
            new_distance = distances[node] + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance

    return distances


def run_134() -> None:
    print("\nPROGRAM 134: SHORTEST PATH IN A DAG")

    vertices = 6
    edges = [
        (0, 1, 5),
        (0, 2, 3),
        (1, 3, 6),
        (1, 2, 2),
        (2, 4, 4),
        (2, 5, 2),
        (2, 3, 7),
        (3, 4, -1),
        (4, 5, -2)
    ]

    source = 0
    distances = dag_shortest_path(vertices, edges, source)

    if distances is None:
        print("The graph contains a cycle. It is not a DAG.")
    else:
        print("Source vertex:", source)
        print("Shortest distances:")

        for vertex, distance in enumerate(distances):
            print(f"Vertex {vertex}: {distance}")


# ---------------------------------------------------------
# PROGRAM 135: CHEAPEST FLIGHTS WITHIN K STOPS
# ---------------------------------------------------------

def cheapest_flight(
    vertices: int,
    flights: list[tuple[int, int, int]],
    source: int,
    destination: int,
    k: int
) -> int:
    """
    Find the cheapest price using at most K intermediate stops.

    Each flight is (from_city, to_city, price).

    At most K stops means at most K + 1 flight edges.
    Returns -1 if no valid route exists.
    """

    if vertices <= 0:
        raise ValueError("Number of vertices must be positive.")

    if not (0 <= source < vertices and 0 <= destination < vertices):
        raise ValueError("Invalid source or destination.")

    if k < 0:
        raise ValueError("K cannot be negative.")

    for u, v, price in flights:
        if not (0 <= u < vertices and 0 <= v < vertices):
            raise ValueError("Flight contains an invalid city.")
        if price < 0:
            raise ValueError("Flight prices cannot be negative.")

    distances: list[float] = [float("inf")] * vertices
    distances[source] = 0

    # At most K + 1 edges can be used.
    for _ in range(k + 1):
        next_distances = distances.copy()
        updated = False

        for u, v, price in flights:
            if distances[u] != float("inf"):
                new_price = distances[u] + price

                if new_price < next_distances[v]:
                    next_distances[v] = new_price
                    updated = True

        distances = next_distances

        if not updated:
            break

    if distances[destination] == float("inf"):
        return -1

    return int(distances[destination])


def run_135() -> None:
    print("\nPROGRAM 135: CHEAPEST FLIGHTS WITHIN K STOPS")

    vertices = 4
    flights = [
        (0, 1, 100),
        (1, 2, 100),
        (2, 3, 100),
        (0, 2, 500),
        (1, 3, 600)
    ]

    source = 0
    destination = 3
    k = 1

    price = cheapest_flight(
        vertices,
        flights,
        source,
        destination,
        k
    )

    print("Source city:", source)
    print("Destination city:", destination)
    print("Maximum intermediate stops:", k)

    if price == -1:
        print("No valid flight route exists.")
    else:
        print("Cheapest flight price:", price)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main() -> None:
    programs = {
        131: run_131,
        132: run_132,
        133: run_133,
        134: run_134,
        135: run_135
    }

    while True:
        print("\n" + "=" * 55)
        print("MONTH 11 - DAY 27: SHORTEST PATH ALGORITHMS")
        print("=" * 55)

        print("131. Dijkstra's Algorithm")
        print("132. Bellman-Ford Algorithm")
        print("133. Floyd-Warshall Algorithm")
        print("134. Shortest Path in a DAG")
        print("135. Cheapest Flights Within K Stops")
        print("136. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Exiting Day 27 programs. Goodbye!")
            break

        if choice == 136:
            for program in programs.values():
                program()
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice. Please select 131-136 or 0.")


if __name__ == "__main__":
    main()
