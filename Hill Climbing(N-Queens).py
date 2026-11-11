
import random


def cost(board):
    n = len(board)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def hill_climbing(n):
    step = 0

    while True:
        board = list(range(n))
        random.shuffle(board)

        print("\nNew random board:")
        print("Step", step)
        print_board(board)
        print("Cost:", cost(board))

        while True:
            current_cost = cost(board)

            if current_cost == 0:
                print("\nSolution found!")
                return board

            best_cost = current_cost
            best_board = board[:]

            for col in range(n):
                for row in range(n):
                    if board[col] == row:
                        continue

                    neighbor = board[:]
                    neighbor[col] = row

                    new_cost = cost(neighbor)

                    if new_cost < best_cost:
                        best_cost = new_cost
                        best_board = neighbor[:]

            if best_cost >= current_cost:
                print("\nLocal minimum reached. Restarting...")
                break

            board = best_board
            step += 1

            print("\nStep", step)
            print_board(board)
            print("Cost:", cost(board))


n = int(input("Enter number of queens: "))

if n == 1 or n >= 4:
    solution = hill_climbing(n)

    print("\nFinal Solution:", solution)
    print("Final Cost:", cost(solution))
    print("\nFinal Chessboard:")
    print_board(solution)
else:
    print("No solution exists for this value of N.")
