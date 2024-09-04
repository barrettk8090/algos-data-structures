# Rotate a Matrix by 180 degrees 
# Given a square matrix, the task is that we turn it by 180 degrees in an anti-clockwise direction without using any extra space. 

# Example Input: 
#                    C0    C1    C2
# 1 2 3             [0,0] [0,1] [0,2] Row 0
# 4 5 6             [1,0] [1,1] [1,2] Row 1 
# 7 8 9             [2,0] [2,1] [2,2] Row 2 

# Example Output
# 9 8 7 
# 6 5 4
# 3 2 1

matrix_ex = [[1,2,3], [4,5,6], [7,8,9]]
# goal: matrix = [[9,8,7], [6,5,4], [3,2,1]]
# Notes: Rows are reversed, columns are reversed 

def rotate_matrix(matrix):
    n = len(matrix)

    # Can start by reversing each row - rows go left to right 
    for i in range(n): 
        left = 0
        right = n - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
        
    #Reverse the order of rows
    top = 0
    bottom = n - 1
    while top < bottom:
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top += 1
        bottom -= 1
    
rotate_matrix(matrix_ex)
print("\nRotated matrix:")
for row in matrix_ex:
    print(row)