import random
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False
def is_draw(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])
def human_move(board):
    while True:
        move = input("Enter a number (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("Spot taken. Try another.")
        else:
            print("Invalid input. Try again.")
def minimax(board, depth, is_maximizing):
    # Base cases for recursion
    if check_win(board, "O"):  # Computer wins
        return 1
    if check_win(board, "X"):  # Human wins
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = str(i * 3 + j + 1)  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:  
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = str(i * 3 + j + 1)  # Undo the move
                    best_score = min(score, best_score)
        return best_score

def computer_move(board):
    best_score = float('-inf')
    best_move = None
    
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ['X', 'O']:
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = str(i * 3 + j + 1) 
                
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
def tic_tac_toe():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    current_player = "X"
    
    while True:
        print_board(board)
        
        if current_player == "X":
            print("Your move!")
            row, col = human_move(board)
        else:
            print("Computer's move!")
            row, col = computer_move(board)
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            if current_player == "X":
                print("You win!")
            else:
                print("Computer wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
