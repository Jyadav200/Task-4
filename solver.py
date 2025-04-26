# solver.py

def is_valid(board, row, col, num):
    """Check if a number can be placed at (row, col)"""
    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False
    
    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False
    
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def solve_sudoku(board):
    """Solve Sudoku puzzle using backtracking"""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        
                        # Backtrack if no solution found
                        board[row][col] = 0
                return False  # No valid number found, backtrack
    return True  # Puzzle solved
