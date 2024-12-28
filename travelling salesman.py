from itertools import permutations
def tsp_brute_force(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_cost = float('inf')
    best_path = None
    for perm in permutations(vertices):
        current_path = [start] + list(perm) + [start]  
        current_cost = 0
        for i in range(len(current_path) - 1):
            current_cost += graph[current_path[i]][current_path[i + 1]]
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = current_path    
    return best_path, min_cost
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
start_node = 'A'
best_path, min_cost = tsp_brute_force(graph, start_node)
print("Best Path:", " -> ".join(best_path))
print("Minimum Cost:", min_cost)
