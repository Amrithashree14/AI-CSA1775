from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
result = bfs(graph, 'A')
print("BFS Traversal:", result)
