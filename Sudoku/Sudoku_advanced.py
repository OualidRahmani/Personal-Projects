import random

SPARSNESS = 0.5


def show_board(board):
    for i in range(9):
        if i % 3 == 0 and i:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            cell = board[i][j] if board[i][j] != 0 else '.'
            if (j + 1) % 3 == 0 and j != 8:
                print(f" {cell} |", end="")
            elif j == 8:
                print(f" {cell}")
            else:
                print(f" {cell}", end="")


def is_valid(board, r, c, val):
    for j in range(9):
        if board[r][j] == val:
            return False
    for i in range(9):
        if board[i][c] == val:
            return False
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == val:
                return False
    return True


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None


def is_correct(board):
    for row in board:
        vals = [x for x in row if x != 0]
        if len(vals) != len(set(vals)):
            return False
    for j in range(9):
        col = [board[i][j] for i in range(9) if board[i][j] != 0]
        if len(col) != len(set(col)):
            return False
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            square = [
                board[i][j]
                for i in range(br, br+3)
                for j in range(bc, bc+3)
                if board[i][j] != 0
            ]
            if len(square) != len(set(square)):
                return False
    return True


def backtracking_solver(board):
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    nums = list(range(1, 10))
    random.shuffle(nums)
    for val in nums:
        if is_valid(board, r, c, val):
            board[r][c] = val
            if backtracking_solver(board):
                return True
            board[r][c] = 0
    return False


def generate_full_board():
    board = [[0]*9 for _ in range(9)]
    backtracking_solver(board)
    return board


def remove_numbers(board, sparsity):
    for r in range(9):
        for c in range(9):
            if random.random() < sparsity:
                board[r][c] = 0


def get_candidates(board, r, c):
    used = set(board[r])
    used |= {board[i][c] for i in range(9)}
    br, bc = (r // 3) * 3, (c // 3) * 3
    used |= {board[i][j] for i in range(br, br+3) for j in range(bc, bc+3)}
    used.discard(0)
    return [x for x in range(1, 10) if x not in used]


def heuristic_solve(board):
    progress = True
    while progress:
        progress = False
        for r in range(9):
            for c in range(9):
                if board[r][c] != 0:
                    continue
                candidates = get_candidates(board, r, c)
                if len(candidates) == 0:
                    return
                if len(candidates) == 1:
                    board[r][c] = candidates[0]
                    progress = True

        for val in range(1, 10):
            for r in range(9):
                positions = [c for c in range(9) if board[r][c] == 0 and val in get_candidates(board, r, c)]
                if len(positions) == 1:
                    board[r][positions[0]] = val
                    progress = True

            for c in range(9):
                positions = [r for r in range(9) if board[r][c] == 0 and val in get_candidates(board, r, c)]
                if len(positions) == 1:
                    board[positions[0]][c] = val
                    progress = True

            for br in range(0, 9, 3):
                for bc in range(0, 9, 3):
                    positions = [
                        (i, j)
                        for i in range(br, br+3)
                        for j in range(bc, bc+3)
                        if board[i][j] == 0 and val in get_candidates(board, i, j)
                    ]
                    if len(positions) == 1:
                        board[positions[0][0]][positions[0][1]] = val
                        progress = True


B = generate_full_board()

print("Full valid board:")
show_board(B)

remove_numbers(B, SPARSNESS)

print("\nPuzzle:")
show_board(B)

print("\nHeuristic solving...\n")
heuristic_solve(B)

if not is_correct(B):
    print("\nBacktracking solving...\n")
    backtracking_solver(B)

show_board(B)