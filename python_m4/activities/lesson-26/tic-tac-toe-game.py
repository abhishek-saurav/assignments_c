board = [" "] * 9
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
player = "X"
moves = 0
winner = ""

while winner == "" and moves < 9:
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    spot = int(input(player + " choose a spot (0-8): "))
    if board[spot] != " ":
        print("Spot taken, try again")
        continue
    board[spot] = player
    moves = moves + 1
    for a, b, c in wins:
        if board[a] == player and board[b] == player and board[c] == player:
            winner = player
    if player == "X":
        player = "O"
    else:
        player = "X"

if winner == "":
    print("It's a draw!")
else:
    print(winner, "wins!")
