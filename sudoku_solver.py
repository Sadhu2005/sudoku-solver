def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if board[row][i] == num:
            return False
        
    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True
def print_board(board):
    for row in range(9):
        for col in range(9):
            print(board[row][col], end=" ")
        print()
# Example Sudoku board (0 represents empty cells)
"""board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]"""
#above the comment when i give the example board for testing
#now i want to take in put from the user ....-sadhu 
def create_empty_sudoku_board():
    return [[0 for _ in range(9)] for _ in range(9)]

def print_sudoku_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def get_user_input():
    print("Enter the Sudoku board row by row (use '0' for empty cells):")
    board = []
    for i in range(9):
        while True:
            row_input = input(f"Enter row {i + 1} (9 numbers separated by spaces): ")
            numbers = row_input.split()
            if len(numbers) == 9 and all(num.isdigit() and 0 <= int(num) <= 9 for num in numbers):
                board.append([int(num) for num in numbers])
                break
            else:
                print("Invalid input. Please enter 9 numbers between 0 and 9.")
    return board

# Get user input to fill the Sudoku board
sudoku_board = get_user_input()

# Display the entered Sudoku board
print("\nThe entered Sudoku board is:")
print_sudoku_board(sudoku_board)

if solve_sudoku(board):
    print("Sudoku solved:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku board.")
    