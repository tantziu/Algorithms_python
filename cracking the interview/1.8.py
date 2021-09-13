def zero_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    zeros = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                zeros.append((i, j))

    for i in range(len(zeros)):
        zero_row(matrix, zeros[i][0])
        zero_column(matrix, zeros[i][1])
    return matrix


def zero_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0


def zero_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9], [3, 0, 6]]
print(zero_matrix(matrix))
