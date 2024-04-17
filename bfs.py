from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)

    while queue:
        node, path = queue.popleft()
        print("Visited:", node)
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

path = bfs(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("Path not found.")
