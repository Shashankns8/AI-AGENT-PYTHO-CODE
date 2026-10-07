GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    row = zero_pos // 3
    col = zero_pos % 3
    moves = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)    
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = \
                new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    return neighbors
def depth_limited_search(state, depth, path):
    if state == GOAL:
        return path
    if depth == 0:
        return None
    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = depth_limited_search(
                neighbor,
                depth - 1,
                path + [neighbor]
            )
            if result is not None:
                return result
    return None
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()
def ids(start):
    depth = 0
    while True:
        result = depth_limited_search(
            start,
            depth,
            [start]
        )
        if result is not None:
            return result
        depth += 1
start = (1, 2, 3,
         0, 4, 6,
         7, 5, 8)
print("INITIAL STATE")
print_puzzle(start)
print("========== IDS ==========")
ids_solution = ids(start)
print("Number of moves:", len(ids_solution) - 1)
for i, state in enumerate(ids_solution):
    print("Step", i)
    print_puzzle(state)
