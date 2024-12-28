from collections import deque
def is_valid_state(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:  
        return False
    if (m < c and m > 0) or (3 - m < 3 - c and 3 - m > 0):  
        return False
    return True
def bfs():
    initial_state = (3, 3, 0)  
    goal_state = (0, 0, 1)     
    queue = deque([(initial_state, [])])  
    visited = set([initial_state])        
    while queue:
        (m, c, b), path = queue.popleft()
        if (m, c, b) == goal_state:
            return path + [(m, c, b)]
        moves = [
            (-2, 0), (-1, 0), (0, -2), (1, 0), (0, 1), (0, -1)  
        ]      
        for dm, dc in moves:
            if b == 0:  
                new_m, new_c = m + dm, c + dc
            else:  
                new_m, new_c = m - dm, c - dc          
            if is_valid_state(new_m, new_c):
                new_state = (new_m, new_c, 1 - b)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [(m, c, b)]))
    return None  
solution = bfs()
if solution:
    print("Solution found:")
    for step in solution:
        print(f"Missionaries: {step[0]}, Cannibals: {step[1]}, Boat: {'Left' if step[2] == 0 else 'Right'}")
else:
    print("No solution found.")
