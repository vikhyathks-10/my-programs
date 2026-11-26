
from collections import deque


# ============================================================
# PROGRAM 126: TOPOLOGICAL SORT USING DFS
# Find a valid topological ordering using DFS.
# Return an empty list if the graph contains a cycle.
# ============================================================

def topological_sort_dfs(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[int]:

    graph: list[list[int]] = [[] for _ in range(vertices)]

    for u, v in edges:
        graph[u].append(v)

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * vertices
    stack: list[int] = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle

        state[node] = 1

        for neighbour in graph[node]:

            if state[neighbour] == 0:
                dfs(neighbour)

            elif state[neighbour] == 1:
                # Back edge means a directed cycle.
                has_cycle = True

        state[node] = 2
        stack.append(node)

    for vertex in range(vertices):
        if state[vertex] == 0:
            dfs(vertex)

    if has_cycle:
        return []

    return stack[::-1]


def demo_126() -> None:
    vertices = 6

    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    print("Vertices:", vertices)
    print("Directed Edges:", edges)

    result = topological_sort_dfs(vertices, edges)

    if result:
        print("\nTopological Order:", result)
    else:
        print("\nTopological ordering does not exist (cycle detected).")


# ============================================================
# PROGRAM 127: TOPOLOGICAL SORT USING KAHN'S ALGORITHM
# Use indegree calculation and BFS queue.
# ============================================================

def topological_sort_kahn(
    vertices: int,
    edges: list[tuple[int, int]]
) -> list[int]:

    graph: list[set[int]] = [set() for _ in range(vertices)]
    indegree = [0] * vertices

    for u, v in edges:
        if v not in graph[u]:
            graph[u].add(v)
            indegree[v] += 1

    queue: deque[int] = deque()

    # Add all vertices having indegree zero.
    for vertex in range(vertices):
        if indegree[vertex] == 0:
            queue.append(vertex)

    result: list[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # If all vertices are not processed, a cycle exists.
    if len(result) != vertices:
        return []

    return result


def demo_127() -> None:
    vertices = 6

    edges = [
        (5, 2),
        (5, 0),
        (4, 0),
        (4, 1),
        (2, 3),
        (3, 1)
    ]

    print("Vertices:", vertices)
    print("Directed Edges:", edges)

    result = topological_sort_kahn(vertices, edges)

    if result:
        print("\nTopological Order:", result)
    else:
        print("\nTopological ordering does not exist (cycle detected).")


# ============================================================
# PROGRAM 128: COURSE SCHEDULE
# Determine whether all courses can be completed.
# A prerequisite must be completed before its course.
# ============================================================

def can_finish_courses(
    number_of_courses: int,
    prerequisites: list[tuple[int, int]]
) -> bool:

    graph: list[set[int]] = [
        set() for _ in range(number_of_courses)
    ]

    indegree = [0] * number_of_courses

    # (course, prerequisite) means prerequisite -> course.
    for course, prerequisite in prerequisites:
        if course not in graph[prerequisite]:
            graph[prerequisite].add(course)
            indegree[course] += 1

    queue: deque[int] = deque()

    for course in range(number_of_courses):
        if indegree[course] == 0:
            queue.append(course)

    completed = 0

    while queue:
        course = queue.popleft()
        completed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    return completed == number_of_courses


def demo_128() -> None:
    number_of_courses = 4

    prerequisites = [
        (1, 0),
        (2, 1),
        (3, 2)
    ]

    print("Number of Courses:", number_of_courses)
    print("Prerequisites:", prerequisites)

    result = can_finish_courses(
        number_of_courses,
        prerequisites
    )

    print("\nCan Finish All Courses:", result)

    # Demonstrate a cyclic prerequisite example.
    cyclic_prerequisites = [
        (1, 0),
        (2, 1),
        (0, 2)
    ]

    print("\nCyclic Prerequisites:", cyclic_prerequisites)

    print(
        "Can Finish All Courses:",
        can_finish_courses(3, cyclic_prerequisites)
    )


# ============================================================
# PROGRAM 129: COURSE SCHEDULE II
# Return a valid order in which all courses can be completed.
# ============================================================

def find_course_order(
    number_of_courses: int,
    prerequisites: list[tuple[int, int]]
) -> list[int]:

    graph: list[set[int]] = [
        set() for _ in range(number_of_courses)
    ]

    indegree = [0] * number_of_courses

    for course, prerequisite in prerequisites:
        if course not in graph[prerequisite]:
            graph[prerequisite].add(course)
            indegree[course] += 1

    queue: deque[int] = deque()

    for course in range(number_of_courses):
        if indegree[course] == 0:
            queue.append(course)

    order: list[int] = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    if len(order) != number_of_courses:
        return []

    return order


def demo_129() -> None:
    number_of_courses = 4

    prerequisites = [
        (1, 0),
        (2, 0),
        (3, 1),
        (3, 2)
    ]

    print("Number of Courses:", number_of_courses)
    print("Prerequisites:", prerequisites)

    result = find_course_order(
        number_of_courses,
        prerequisites
    )

    if result:
        print("\nValid Course Order:", result)
    else:
        print("\nNo valid course order exists.")


# ============================================================
# PROGRAM 130: ALIEN DICTIONARY
# Determine a possible character order from sorted words.
# ============================================================

def alien_dictionary(words: list[str]) -> str:

    graph: dict[str, set[str]] = {}
    indegree: dict[str, int] = {}

    # Include every character, even isolated characters.
    for word in words:
        for character in word:
            if character not in graph:
                graph[character] = set()
                indegree[character] = 0

    # Compare adjacent words to find character ordering.
    for index in range(len(words) - 1):
        first = words[index]
        second = words[index + 1]

        limit = min(len(first), len(second))

        found_difference = False

        for position in range(limit):
            if first[position] != second[position]:

                char1 = first[position]
                char2 = second[position]

                # char1 must appear before char2.
                if char2 not in graph[char1]:
                    graph[char1].add(char2)
                    indegree[char2] += 1

                found_difference = True
                break

        # Invalid case: longer word appears before its prefix.
        if not found_difference and len(first) > len(second):
            return ""

    # Kahn's algorithm for character ordering.
    queue: deque[str] = deque()

    for character in indegree:
        if indegree[character] == 0:
            queue.append(character)

    order: list[str] = []

    while queue:
        character = queue.popleft()
        order.append(character)

        for neighbour in graph[character]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    # If not all characters are processed, constraints contain a cycle.
    if len(order) != len(indegree):
        return ""

    return "".join(order)


def demo_130() -> None:
    words = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]

    print("Alien Dictionary Words:", words)

    result = alien_dictionary(words)

    if result:
        print("\nPossible Character Order:", result)
    else:
        print("\nNo valid character ordering exists.")


# ============================================================
# MAIN MENU
# ============================================================

def main() -> None:

    programs = {
        126: demo_126,
        127: demo_127,
        128: demo_128,
        129: demo_129,
        130: demo_130
    }

    while True:
        print("\n" + "=" * 65)
        print("MONTH 11 - DAY 26: TOPOLOGICAL SORTING")
        print("=" * 65)

        print("126. Topological Sort Using DFS")
        print("127. Topological Sort Using Kahn's Algorithm")
        print("128. Course Schedule")
        print("129. Course Schedule II")
        print("130. Alien Dictionary")
        print("131. Run All Programs")
        print("0. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            print("Day 26 completed. Keep practicing!")
            break

        elif choice == 131:
            for number in range(126, 131):
                print("\n" + "#" * 65)
                print(f"RUNNING PROGRAM {number}")
                print("#" * 65)
                programs[number]()

        elif choice in programs:
            programs[choice]()

        else:
            print("Invalid choice. Please select 126–131 or 0.")


if __name__ == "__main__":
    main()
