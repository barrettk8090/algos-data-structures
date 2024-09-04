# Matrix transpose
# Transpose is an operation that turns the rows of the original matrix into the columns of the new matrix, and the columns into the rows.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#Input
# 1 2 3 
# 4 5 6 
# 7 8 9

#Expected Output
# 1 4 7 
# 2 5 8 
# 3 6 9 

for i in range (len(matrix)):
    for j in range (len(matrix[0])):
        result[j][i] = matrix[i][j]
print(result)