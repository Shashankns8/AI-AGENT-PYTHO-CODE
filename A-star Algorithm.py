
import heapq


# Calculate Manhattan distance
def manhattan_distance(state, goal):
    distance = 0
    goal_positions = {}

    for i in range(9):
        goal_positions[goal[i]] = divmod(i, 3)

    for i in range(9):
        tile = state[i]

        if tile != 0:
            row, col = divmod(i, 3)
            target_row, target_col = goal_positions[tile]

            distance += abs(row - target_row) + abs(col - target_col)

    return distance


# Generate neighboring states
def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)

            new_state[zero], new_state[new_pos] = (
                new_state[new_pos],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* search algorithm
def a_star(initial, goal):
    open_list = []

    heapq.heappush(
        open_list,
        (manhattan_distance(initial, goal), 0, initial)
    )

    g_cost = {initial: 0}
    parent = {initial: None}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        # Ignore outdated entries
        if g != g_cost.get(current):
            continue

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        # Explore neighbors
        for neighbor in get_neighbors(current):
            new_g = g + 1

            if new_g < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                h = manhattan_distance(neighbor, goal)

                heapq.heappush(
                    open_list,
                    (new_g + h, new_g, neighbor)
                )

    return None


# Print the puzzle as a 3x3 grid
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(*state[i:i + 3])
    print()


# Initial state (solvable)
initial = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Execute the algorithm
path = a_star(initial, goal)

if path is not None:
    print("Solution found!")
    print("Number of moves:", len(path) - 1)
    print("\nSolution steps:\n")

    for step, state in enumerate(path):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution exists.")
