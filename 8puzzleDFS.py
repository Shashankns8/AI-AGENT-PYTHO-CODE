def display(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()


def neighbors(state):

    result = []

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # UP
        (1, 0),    # DOWN
        (0, -1),   # LEFT
        (0, 1)     # RIGHT
    ]

    for dr, dc in moves:

        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:

            new_zero = r * 3 + c

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            result.append(tuple(new_state))

    return result


def dfs(start, goal):

    stack = [(start, [start])]
    visited = set()

    while stack:

        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path

        for next_state in neighbors(state):

            if next_state not in visited:
                stack.append(
                    (next_state, path + [next_state])
                )

    return None


# INPUT
print("Enter the puzzle values:")
print("Use 0 for blank space")

start = tuple(
    map(int, input().split())
)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = dfs(start, goal)

if solution:

    print("\nSolution found!")

    for state in solution:
        display(state)

else:

    print("No solution found")
