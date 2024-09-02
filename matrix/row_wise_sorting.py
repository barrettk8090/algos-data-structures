# Sorting a matrix row-wise 

# Example: Given a 2D array, sort each row of this array and print the result:

# Input 
## 77 11 22 3
## 11 89 1 12
## 32 11 56 7
## 11 22 44 33

# Output 
## 3 11 22 77
## 1 11 12 89
## 7 11 32 56
## 11 22 33 44

# Method 1) Using bubble sort: Start iterating through each row of the given 2D array, and sort elements of each row using an efficient sorting algorithm

def sortRowWise(matrix):

    #loop through the rows of the matrix 
    for i in range(len(matrix)):
        
        # loop through the columns of the matrix
        for j in range(len(matrix[i])):

            # loop for comparison and swapping
            for k in range(len(matrix[i]) - j - 1):
                if (matrix[i][k] > matrix[i][k+1]):

                    # swap the elements
                    t = matrix[i][k]
                    matrix[i][k] = matrix[i][k +1]
                    matrix[i][k+1] = t

    # print the sorted matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()

matrix = [[9, 8, 7, 1 ],[7, 3, 0, 2],[9, 5, 3, 2],[ 6, 3, 1, 2 ]]
sortRowWise(matrix)