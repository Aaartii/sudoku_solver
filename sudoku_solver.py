def solve_sudoku(board):
    # Find the next empty cell (represented by 0)
    row, col = find_empty_cell(board)
    
    # If there are no empty cells, the Sudoku is solved
    if row == -1:
        return True
    
    # Try filling the empty cell with numbers 1 to 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # If the number is valid, place it in the cell
            board[row][col] = num
            
            # Recursively solve the Sudoku
            if solve_sudoku(board):
                return True
            
            # If the current placement leads to an invalid solution,
            # backtrack by resetting the cell and trying the next number
            board[row][col] = 0
    
    # If no number can be placed, the Sudoku is unsolvable
    return False


def find_empty_cell(board):
    # Find the next empty cell in the board
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return -1, -1


def is_valid(board, row, col, num):
    # Check if it's valid to place 'num' in the given cell
    
    # Check row and column constraints
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Check the 3x3 box constraints
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True


def print_board(board):
    # Print the Sudoku board
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


# Example usage:
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Input Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolution:")
    print_board(board)
else:
    print("\nNo solution exists.")
