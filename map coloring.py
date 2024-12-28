def is_valid(node, color, graph, colors):
    """Check if coloring node with color is valid."""
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True
def solve_map_coloring(graph, color_options, colors, node):
    """Recursive function to solve the map coloring problem."""
    if node == len(graph):
        return True
    current_node = list(graph.keys())[node]
    for color in color_options:
        if is_valid(current_node, color, graph, colors):
            colors[current_node] = color  
            if solve_map_coloring(graph, color_options, colors, node + 1):
                return True
            colors[current_node] = None  
    return False
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}
color_options = ["Red", "Green", "Blue"]
colors = {node: None for node in graph}
if solve_map_coloring(graph, color_options, colors, 0):
    print("Solution found:")
    print(colors)
else:
    print("No solution exists.")
