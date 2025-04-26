# main.py

from solver import solve_sudoku

def print_board(board):
    """Print the Sudoku board in a readable format"""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def load_puzzle(filename):
    """Load Sudoku puzzle from a file (puzzle.txt)"""
    board = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = list(map(int, line.split()))
                board.append(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None
    return board

def main():
    puzzle_file = 'puzzle.txt'
    sudoku_grid = load_puzzle(puzzle_file)
    
    if sudoku_grid is None:
        return
    
    print("Sudoku Puzzle (Before Solving):")
    print_board(sudoku_grid)
    
    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku Puzzle:")
        print_board(sudoku_grid)
    else:
        print("\nNo solution exists.")

if __name__ == "__main__":
    main()
