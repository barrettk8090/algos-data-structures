# Math Matrix Basics 

# Addition – Square Matrix 3x3

matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[9,8,7],[6,5,4],[3,2,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        # First pass: result[0][0] = matrix1[0][0] + matrix2[0][0]
                                                # 1 + 9 
print("Addition example: ", result)

# Subtraction – Square Matrix 3x3

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] - matrix2[i][j]
        # First pass: result[0][0] = matrix1[0][0] - matrix2[0][0]
                                                # 1 - 9 
print("Subtraction example:", result)

# Multiplication by a number 

scalar = 2

for i in range (len(matrix1)):
    for j in range (len(matrix1[0])):
        result[i][j] = matrix1[i][j] * scalar
print("Scalar multiplication:", result)

# Multiplication of matrices

matrix3 = [[1,2],[3,4]]
matrix4 = [[5,6],[7,8]]
result2 = [[0,0], [0,0]]

for i in range(len(matrix3)): 
         for j in range(len(matrix4[0])): 
                  # Each time the i and j loops run, k=0 and k=1 (last loop runs fully, in order to calculate sums)
                  for k in range(len(matrix4)): 
                       result2[i][j] += matrix3[i][k] * matrix4[k][j]
print("Multiplying matrices: ", result2)