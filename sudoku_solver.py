def is_valid(sudoku_board, row, col, num):
    # Check if the number already exists in the row
    for i in range(9):
        if sudoku_board[row][i] == num:
            return False
        
    # Check if the number already exists in the column
    for i in range(9):
        if sudoku_board[i][col] == num:
            return False
    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku_board[start_row + i][start_col + j] == num:
                return False
    return True
def solve_sudoku(sudoku_board):
    for row in range(9):
        for col in range(9):
            if sudoku_board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku_board, row, col, num):
                        sudoku_board[row][col] = num
                        if solve_sudoku(sudoku_board):
                            return True
                        sudoku_board[row][col] = 0
                return False
    return True
def print_board(sudoku_board):
    for row in range(9):
        for col in range(9):
            print(sudoku_board[row][col], end=" ")
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
def create_sudoku_board():
    board = []
    print("Enter the Sudoku board (9 rows, each row containing 9 space-separated numbers, use '0' for empty cells):")
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

# Example usage:
sudoku_board = create_sudoku_board()
print("Sudoku board entered:")
for row in sudoku_board:
    print(row)


if solve_sudoku(sudoku_board):
    print("Sudoku solved:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku board.")