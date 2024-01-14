import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def is_valid_move(board, row, col, num):
    # Check if the number is not present in the same row and column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not present in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved successfully

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack if the solution is not found

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the row and column of an empty cell
    return None

def generate_sudoku():
    # Generate a complete Sudoku solution
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)
    
    # Remove some numbers to create a puzzle
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board

def play_sudoku():
    sudoku_board = generate_sudoku()

    print("Welcome to Sudoku!")
    print("Enter your moves in the format 'row col num' (e.g., '3 5 7').")
    print("To quit, type 'quit'.")

    while True:
        print_board(sudoku_board)

        user_input = input("Enter your move: ").lower()

        if user_input == 'quit':
            print("Quitting the game. Goodbye!")
            break

        try:
            row, col, num = map(int, user_input.split())
            if is_valid_move(sudoku_board, row - 1, col - 1, num):
                sudoku_board[row - 1][col - 1] = num
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter three space-separated integers.")

        if all(all(cell != 0 for cell in row) for row in sudoku_board):
            print("Congratulations! You solved the Sudoku!")
            break

if __name__ == "__main__":
    play_sudoku()
