from queue import PriorityQueue

# Function to get user input for the graph
def get_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    print("Enter the edges in the format: Source Destination Cost (e.g., A B 4)")
    print("Type 'done' when finished.")

    while True:
        edge = input("Edge: ").strip()
        if edge.lower() == "done":
            break
        try:
            src, dest, cost = edge.split()
            cost = int(cost)
            if src not in graph:
                graph[src] = []
            graph[src].append((dest, cost))
            if dest not in graph:
                graph[dest] = []
        except ValueError:
            print("Invalid format. Please enter again.")

    return graph

# Function to get user input for heuristic values
def get_heuristics(graph):
    heuristic = {}
    print("\nEnter heuristic values for each node:")
    for node in graph:
        heuristic[node] = int(input(f"Heuristic value for {node}: "))
    return heuristic

# Depth-Limited Search (DLS)
def dls(graph, node, goal, depth, path):
    if depth == 0:
        return None
    path.append(node)
    if node == goal:
        return path
    for neighbor, _ in graph[node]:
        if neighbor not in path:
            result = dls(graph, neighbor, goal, depth - 1, path[:])
            if result:
                return result
    return None

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(graph, start, goal):
    depth = 0
    while True:
        print(f"Searching at depth {depth}...")
        result = dls(graph, start, goal, depth, [])
        if result:
            print(f"Goal '{goal}' found at depth {depth}!")
            return result
        depth += 1

# Best-First Search (Greedy Search)
def best_first_search(graph, start, goal, heuristic):
    print("\n--- Best-First Search (Greedy Search) ---")
    pq = PriorityQueue()
    pq.put((heuristic[start], [start]))  # Priority based on heuristic
    visited = set()

    while not pq.empty():
        _, path = pq.get()
        node = path[-1]

        if node in visited:
            continue
        visited.add(node)

        print(f"Expanding node '{node}' with heuristic {heuristic[node]}")

        if node == goal:
            print(f"Goal '{goal}' reached!")
            return path

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                pq.put((heuristic[neighbor], new_path))

    print("Goal not reachable!")
    return None

# A* Search Algorithm
def a_star(graph, start, goal, heuristic):
    print("\n--- A* Search Algorithm ---")
    pq = PriorityQueue()
    pq.put((0 + heuristic[start], 0, [start]))  # (f = g + h, g, path)
    visited = {}

    while not pq.empty():
        f, g, path = pq.get()
        node = path[-1]

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        print(f"Expanding node '{node}': g={g}, h={heuristic[node]}, f={f}")

        if node == goal:
            print(f"Goal '{goal}' reached with total cost {g}!")
            return path

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_path = path + [neighbor]
            pq.put((new_g + heuristic[neighbor], new_g, new_path))

    print("Goal not reachable!")
    return None

# Get user inputs
graph = get_graph()
heuristic = get_heuristics(graph)

# Get start and goal nodes
start = input("\nEnter the start node: ").strip()
goal = input("Enter the goal node: ").strip()

# Run and print results
iddfs_path = iddfs(graph, start, goal)
best_first_path = best_first_search(graph, start, goal, heuristic)
a_star_path = a_star(graph, start, goal, heuristic)

# Run DLS with a specific depth
depth_limit = int(input("\nEnter depth limit for Depth-Limited Search (DLS): "))
dls_path = dls(graph, start, goal, depth_limit, [])
if dls_path:
    print(f"Goal '{goal}' found within depth {depth_limit}!")
else:
    print(f"Goal '{goal}' not found within depth {depth_limit}.")

# Final summary of results
print("\n--- Final Results Summary ---")
print(f"DLS Path Found (Depth {depth_limit}): {dls_path}")
print(f"IDDFS Path Found: {iddfs_path}")
print(f"Best-First Search Path Found: {best_first_path}")
print(f"A* Search Path Found: {a_star_path}")
