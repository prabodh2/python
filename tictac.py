#wap to play tic tac toe
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
currentPlayer = 'X'

def displayBoard():
    for i in board:
        print(end="|")
        for j in i:
            print(j, end="|")
        print()

def checkDraw():
    for i in board:
        if " " in i:
            return False
    return True

def checkWin(player):

    displayBoard()

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            print(f"{player} wins")
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            print(f"{player} wins")
            return True
    
    if board[0][0] ==board[i][1] == board[i][2] == player:
            print(f"{player} wins")
            return True
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            print(f"{player} wins")
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        print(f"{player} wins")
        return True
    
    return False

while(not checkWin(currentPlayer)):

    if (checkDraw()):
        print("Game over!!! It's draw")
        break

    currentPlayer = 'O' if currentPlayer == 'X' else 'X'

    print(f"Current player:- {currentPlayer}")
    row = int(input("Select the row: "))
    col = int(input("Select the col: "))
    while(board[row][col] != " "):
        print("Invalid input Try again!!!")
        row = int(input("Select the row: "))
        col = int(input("Select the col: "))
    board[row][col] = currentPlayer