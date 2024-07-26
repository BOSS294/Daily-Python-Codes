def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0]!= " ":
            return True
            
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column]!= " ":
            return True
            
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!= " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]!= " ":
        return True
        
    return False
    
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
                
    return True
    
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = {"X": "Anjali", "O": "Abhinav"}
    current_player = "X"
    
    while True:
        print_board(board)
        print("Player {}, enter your move (row and column number, 0-2)".format(players[current_player]))
        row = int(input("Row: "))
        col = int(input("Column: "))
        
        if board[row][col]!= " ":
            print("Invalid move, try again.")
            continue
        
        board[row][col] = current_player
        
        if check_winner(board):
            print_board(board)
            print("{} Wins".format(players[current_player]))
            break
        elif is_board_full(board):
            print_board(board)
            print("It is a tie!")
            break
        
        current_player = "X" if current_player == "O" else "O"

tic_tac_toe()
