#Traversing a Matrix Data Structure
# Below we have three rows and four columns:
    #Rows: [1,2,3,4] and [5,6,7,8] and [9,10,11,12]
    #Columns: Think of columns as the first num in each inner array
            # 1 2 3 4 
            # 5 6 7 8
            # 9 10 11 12
    # 1,5,9 and 2,6,10 and 3,7,11 and 4,8,12
traversal_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# Traversing over all the rows
for i in range(0,3):
    # Traversing over all the columns of each row
    for j in range(0,4):
        print(traversal_arr[i][j], end=" ")

#Reads as:
    # [0,0]
    # [0,1]
    # [0,2]
    # [0,3]
    # Hits j range limit, so i range switches to 1
    # [1,0]
    # [1,1]
    # [1,2]
    # [1,3]

def traversal_function(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")

new_matrix = [[4,5,6,7],[8,9,10,11],[12,13,14,15]]
traversal_function(new_matrix)