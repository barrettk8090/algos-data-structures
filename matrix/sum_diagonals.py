# Write a function that takes a square matrix and returns the sum of its diagonals
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# 1, 5, 9 = 15
# 7, 5, 3 = 15
# Sum of diagonals = 30

matrix_one = [[1,2,3], [4,5,6], [7,8,9]]

def sum_diagonals(matrix):
    # n = 3
    n = len(matrix)
    # main_diagonal - get the sum of [0][0] (1), [1][1] (5), [2][2] (9)
    main_diagonal = sum(matrix[i][i] for i in range (n))
    # second_diagonal - get the sum of [0][2] (3), [1][1] (5), [2][0] (7)
    second_diagonal = sum(matrix[i][n-1-i] for i in range(n))
    print(main_diagonal + second_diagonal)
    return main_diagonal + second_diagonal

sum_diagonals(matrix_one)

matrix_two = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [12,14,15,16]
]

sum_diagonals(matrix_two)