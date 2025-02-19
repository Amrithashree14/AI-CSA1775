def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True
def solve_n_queens_one_solution(board, row, n):
    if row == n:
        print_solution(board)
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  
            if solve_n_queens_one_solution(board, row + 1, n):
                return True
            board[row][col] = 0 
    return False
def eight_queens_one_solution():
    n = 8
    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_one_solution(board, 0, n):
        print("No solution exists.")
eight_queens_one_solution()
