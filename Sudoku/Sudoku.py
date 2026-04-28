import random

SPARSNESS = 0.4

def zero_popper(values):
    return [x for x in values if x != 0]

def show_board(board):
    for i in range(9):
        if not(i % 3) and (i):
            print("- - - - - - - - - - - - ")
        for j in range(9):
            cell = board[i][j] if board[i][j] != 0 else '.'
            if (j + 1) % 3 == 0 and j != 8 : print(f" {cell} |", end = "")
            elif j == 8 : print(f" {cell}")
            else : print(f" {cell}", end = "")


# def randomIntegerGeneration(inputs,weights):
#     """
#     inputs is the sorted list of inputs
#     weights is the list of weights
#     """
#     if len(inputs) == 1 :
#         return inputs[0]

#     L = [x for x in weights]
#     for i in range(1,len(weights)):
#         L[i] += L[i-1]

#     probs = [x / L[- 1] for x in L]

#     r = random()

#     for i in range(len(probs)):
#         if probs[i] > r:
#             return inputs[i]


# def generateWeights(inputs):
#     L = [0]*(len(inputs))
#     return [x + random() for x in L]



# def rand_list():
#     L = [1,2,3,4,5,6,7,8,9]
#     line = []

#     while len(L) > 0 :
#         i = random.choice(L)
#         line.append(i)
#         L.remove(i)

#     for k in range(9):
#         if random.random() <= SPARSNESS :
#             line[k] = 0
#     return line

def rand_list():
    line = list(range(1, 10))
    random.shuffle(line)

    return [x if random.random() > SPARSNESS else 0 for x in line]

def generate_board():
    return [rand_list() for _ in range(9)]


def linear_board(board):
    return [board[i][j] for i in range(9) for j in range(9)]

def is_row_correct(board):
    for i in range(9):
        row = board[i]
        row0 = zero_popper(row)
        if len(row0) != len(set(row0)) :
            return False, i
    return True, -1


def is_column_correct(board):
    for i in range(9):
        col = [board[k][i] for k in range(9)]
        col0 = zero_popper(col)
        if len(col0) != len(set(col0)):
            return False, i
    return True, -1


def is_square_correct(board):
    for brow in range(0,9,3):
        for bcol in range(0,9,3):
            square = [board[p][q]
            for p in range(brow,brow + 3)
            for q in range(bcol,bcol + 3)]
            square0 = zero_popper(square)
            if len(square0) != len(set(square0)):
                return False, (brow, bcol)
    return True, (-1, -1)


def is_correct(board):
    return is_row_correct(board)[0] and is_column_correct(board)[0] and is_square_correct(board)[0]

def get_possible_values(values):
    return [x for x in range(1, 10) if x not in values]

def fix_duplicates(values):
    """
    Fix one duplicate in a list of 9 values.
    Returns True if a fix was applied.
    """
    seen = set()
    duplicates = []

    for idx, v in enumerate(values):
        if v == 0:
            continue
        if v in seen:
            duplicates.append(idx)
        else:
            seen.add(v)

    if not duplicates:
        return False

    k = random.choice(duplicates)
    vals = get_possible_values(values)

    if not vals:
        vals = list(range(1, 10))

    values[k] = random.choice(vals)
    return True

def fix_row(board):
    ok, idx = is_row_correct(board)
    if not ok:
        return fix_duplicates(board[idx])
    return False


def fix_column(board):
    ok, idx = is_column_correct(board)
    if not ok:
        col = [board[r][idx] for r in range(9)]
        if fix_duplicates(col):
            for r in range(9):
                board[r][idx] = col[r]
            return True
    return False


def fix_square(board):
    ok, (br, bc) = is_square_correct(board)
    if not ok:
        square = [board[r][c] for r in range(br, br+3) for c in range(bc, bc+3)]
        if fix_duplicates(square):
            for i in range(9):
                r = br + i // 3
                c = bc + i % 3
                board[r][c] = square[i]
            return True
    return False

def correction_board(board):
    counter = 0

    while not is_correct(board):
        counter += 1

        if counter > 50000:
            print("Repair stopped (too many iterations).")
            return

        if fix_row(board):
            continue

        if fix_column(board):
            continue

        if fix_square(board):
            continue

B = generate_board()

show_board(B)
print("")
print("")
print("")
correction_board(B)
show_board(B)