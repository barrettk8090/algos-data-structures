matrix1 = [[1,2,3],[4,5,6],[7,8,9]]

# 1 2 3     [0,0] [0,1] [0,2]
# 4 5 6     [1,0] [1,1] [1,2]
# 7 8 9     [2,0] [2,1] [2,2]

# 1 + 5 + 9 [0,0] + [1,1] + [2,2] –– increasing row, increasing column
# 7 + 5 + 3 [0,2] + [1,1] + [2,0] –– increasing row, decreasing column

# sum of diagonals

def sum_diagonals(matrix):
    n = len(matrix)
    main_diagonal = sum(matrix[i][i] for i in range(n))
    second_diagonal = sum(matrix[i][n-1-i] for i in range(n))
    total = main_diagonal + second_diagonal
    print("Sum diagonals: ", total)

sum_diagonals(matrix1)

# print everything in one line 

def matrix_printer(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")

matrix_printer(matrix1)

# addition 

matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
matrix3 = [[9,8,7],[6,5,4],[3,2,1]]
added = [[0,0,0],[0,0,0],[0,0,0]]

def matrix_addition(first, second):
    for i in range(len(first)):
        for j in range(len(first[0])):
            added[i][j] = first[i][j] + second[i][j]
    print(added)

matrix_addition(matrix2, matrix3)

