import math

# Initialize the board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Winning combinations: 3 rows, 3 cols, 2 diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    """Checks if there are any empty spaces left."""
    return ' ' not in board

def get_available_moves(board):
    """Returns a list of indices that are still empty."""
    return [i for i, spot in enumerate(board) if spot == ' ']

def minimax(board, depth, is_maximizing):
    """
    The Minimax algorithm. 
    Returns the optimal score for a given board state.
    """
    # Base cases: Check for terminal states (Win, Lose, Tie)
    if check_winner(board, 'O'):  # AI wins
        return 10 - depth
    if check_winner(board, 'X'):  # Human wins
        return depth - 10
    if is_board_full(board):      # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'  # AI makes a simulated move
            score = minimax(board, depth + 1, False)
            board[move] = ' '  # Undo the move
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'  # Human makes a simulated move
            score = minimax(board, depth + 1, True)
            board[move] = ' '  # Undo the move
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    """Finds the best possible move for the AI."""
    best_score = -math.inf
    best_move = None
    
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move

def play_game():
    """Main loop to play the game against the AI."""
    print("Welcome to Tic-Tac-Toe against the Minimax AI!")
    print("You are 'X' and the AI is 'O'.")
    print("Positions are numbered 0-8, reading left-to-right, top-to-bottom.")
    print_board(['0', '1', '2', '3', '4', '5', '6', '7', '8']) # Show position guide
    
    while True:
        # Human Player ('X') Turn
        try:
            human_move = int(input("Enter your move (0-8): "))
            if board[human_move] != ' ':
                print("That space is already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
            continue
            
        board[human_move] = 'X'
        
        if check_winner(board, 'X'):
            print_board(board)
            print("You win! (Wait, this shouldn't happen against a perfect AI...)")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # AI Player ('O') Turn
        print("\nAI is thinking...")
        ai_move = find_best_move(board)
        board[ai_move] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
