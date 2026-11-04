import random
import math

def heuristic(state):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):

            if state[i] == state[j]:
                conflicts += 1

            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def random_successor(state):
    next_state = state.copy()

    col = random.randint(0, 7)
    row = random.randint(0, 7)

    next_state[col] = row

    return next_state


def simulated_annealing():

    current = [random.randint(0, 7) for i in range(8)]

    T = 100
    minimum_temperature = 0.001

    while T > minimum_temperature:

        if heuristic(current) == 0:
            return current

        next_state = random_successor(current)

        delta = heuristic(current) - heuristic(next_state)

        if delta > 0:
            current = next_state

        else:
            probability = math.exp(delta / T)

            if random.random() < probability:
                current = next_state

        T = T * 0.99

    if heuristic(current) == 0:
        return current

    return None


solution = simulated_annealing()

if solution is not None:
    print("Solution found:")

    for row in range(8):
        for col in range(8):

            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

else:
    print("Solution not found. Try running again.")