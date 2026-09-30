board = [" "] * 9

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def winner(p):
    win = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == p:
            return True
    return False


for turn in range(9):

    display()

    p = "X" if turn % 2 == 0 else "O"

    pos = int(input("Player " + p + ", enter position (1-9): ")) - 1

    if board[pos] != " ":
        print("Position already occupied!")
        continue

    board[pos] = p

    if winner(p):
        display()
        print("Player", p, "wins!")
        break

else:
    display()
    print("Draw!")