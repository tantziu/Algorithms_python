def valid_row(board, row):
    seen = set()
    for column in range(0, 9):
        if board[row][column] in seen:
            return False
        if board[row][column] != '.':
            seen.add(board[row][column])
    return True


def valid_column(board, column):
    seen = set()
    for row in range(0, 9):
        if board[row][column] in seen:
            return False
        if board[row][column] != '.':
            seen.add(board[row][column])
    return True


def valid_box(board, row, column):
    seen = set()
     
    for i in range(0, 3):
        for j in range(0, 3):
            cell = board[row+i][column+j]
            if cell in seen:
                return False
            if cell != '.':
                seen.add(cell)
    return True


def valid_row_column_box(m, row, column):
    return (valid_row(m, row) and valid_column(m, column) and 
        valid_box(m, row - row % 3, column - column % 3))


def valid_sudoku(m):
    for i in range(0, 9):
        for j in range(0, 9):
            if not valid_row_column_box(m, i, j):
                return False
    
    return True


# ---------------------------------------------------------
# Solve a sudoku board
def elements_frequency(m):
    dictionary = {}
    for i in range(0, 9):
        for j in range(0, 9):
            if m[i][j] in dictionary:
                dictionary[m[i][j]] += 1
            else:
                dictionary[m[i][j]] = 1
    return dictionary


def empty_cells(dictionary):
    return dictionary.get('.')


def digits_frequency(m):
    elements = elements_frequency(m)
    digits = {}
    for key,value in elements.items():
        if key not in ['.']:
            digits[key] = value
    return digits


def get_maximum_frequency(dictionary):
    maximum_frequency = max(dictionary.values())
    return list(dictionary.keys())[list(dictionary.values()).index(maximum_frequency)]


def seen_in_row(m, row):
    seen = set()
    for column in range(0,9):
        if m[row][column] != '.':
            seen.add(m[row][column])
    return seen


def seen_in_column(m, column):
    seen = set()
    for row in range(0, 9):
        if m[row][column] != '.':
            seen.add(m[row][column])
    return seen


def seen_in_box(m, row, column):
    seen = set()
    for i in range(0, 3):
        for j in range(0, 3):
            cell = m[row+i][j+column]
            if cell != '.':
                seen.add(cell)
    return seen


def valid_row_column_box(m, digit, row, column):
    set1 = seen_in_row(m, row)
    set2 = seen_in_column(m, column)
    set3 = seen_in_box(m, row-row%3, column-column%3)
    # print("set1:",set1)
    # print("set2:", set2)
    # print("set3:", set3)
    if digit in  set1 or digit in set2 or digit in set3:
        return False

    return True


def fill_with_max(m, digit):
    for i in range(0, 9):
        for j in range(0, 9):
            if m[i][j] == '.' and valid_row_column_box(m, digit, i, j):
                # print('Potentianl cell for max i, j:', i, j)
                # check if safe to assign:
                if safe_to_assign(m, digit, i-i%3, j-j%3):
                    m[i][j] = digit


def safe_to_assign(m, digit, row, column):
    empty_spaces_in_box = 9 - len(seen_in_box(m, row, column))
    # print("empty_spaces_in_box:", empty_spaces_in_box)
    possible_assignment = [] 
    for i in range(0, 3):
        for j in range(0, 3):
            cell = m[row+i][j+column]

            if cell == '.':
                if digit not in seen_in_row(m, row) and digit not in seen_in_column(m, column):
                    possible_assignment.append(m[i][j])
    if len(possible_assignment) > 1:
        return False
    return True


def print_board(board):
    for i in range(0, 9):
        for j in range(0,9):
            print(board[i][j], end=' ')
        print('\n')


def solve_sudoku(board):
    used_digits = set()
    digits_dictionary = digits_frequency(board)

    # block to repeat
    while len(used_digits) < 9:
        # something missing, maximum should be adjusted:
        for key in used_digits:
            if key in digits_dictionary and digits_dictionary[key] == 9:
                del digits_dictionary[key]

        # print(digits_dictionary)
        maximum = get_maximum_frequency(digits_dictionary)
        print("max: ", maximum)
    # print("box:",seen_in_box(board, 6, 0))
    # print("row:",seen_in_row(board, 4))
    # print("column:", seen_in_column(board, 2))
        fill_with_max(board, maximum)
        used_digits.add(maximum)
    
    print_board(board)
    print()




board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# output: True

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
# Output: false

# print(valid_sudoku(board1))
print(solve_sudoku(board1))