def rotate_matrix(matrix):
    n = len(matrix)
    print(n)

    for i in range(n):
        for j in range(i, n):
            bucket = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = bucket

    for i in range(n):
        for j in range(int(n / 2)):
            bucket = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = bucket
    return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(matrix))
