unspiraled_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Function should return: [1,2,3,6,9,8,7,4,5]
# 1 2 3 
# 4 5 6
# 7 8 9

# ---
#|-- |
#|___|

# [0,0] [0,1] [0,2]
# [1,0] [1,1] [1,2]
# [2,0] [2,1] [2,2]

# [0,0] [0,1] [0,2] [1, 2] [2,2] [2,1] [2,0] [1,0] [1,1]
# All of first row 
# Third of second row 
# Third of third row
# Second of third row 
# First of third row
# First of second row
# Second of second row 

# FOLLOWS THIS PATTERN: RIGHT, DOWN, LEFT, UP, RIGHT 

def spiral_matrix(matrix):
    if not matrix:
        return []
    
    # create a new array to store result
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:    
        # Traverse right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse down 
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse left
        for i in range(top, left -1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
        
        if left <= right:
            # Traverse up
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1 
        print(result)
        return result
        

spiral_matrix(unspiraled_matrix)
