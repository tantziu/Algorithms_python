
def print_image(m):
    for i in range(len(m)):
        for j in range(len(m)):
            print(m[i][j], end=' ')
        print('\n')

def transpose_matrix(m):
    for i in range(len(m)):
        for j in range(i, len(m)):
            temp = m[i][j]
            m[i][j] = m[j][i]
            m[j][i] = temp
            # m[i][j], m[j][i]= m[j][i], m[i][j]
    return m

# reverse rows
def reverse_image(m):
    for i in range(len(m)):
        for j in range(len(m)//2):
            temp = m[i][j]
            m[i][j] = m[i][len(m)-1-j]
            m[i][len(m)-1-j] = temp


if __name__ == "__main__":
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    # Output: [[7,4,1],[8,5,2],[9,6,3]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    # print_image(matrix1)
    # rotate_image(matrix1)
    t = transpose_matrix(matrix2)
    print_image(t)
    reverse_image(t)
    print_image(t)