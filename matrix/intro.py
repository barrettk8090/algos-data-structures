# Defining number of rows and columns in matrix

# Here, rows = 3, columns = 3
rows, cols = (3,3)
arr = [[0]*cols]*rows
print(arr)
# You could also initirlize it this way: 
# arr = [[0 for j in range(cols)] for i in range(rows)]


# Inititalizing a new matrix
new_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 1 2 3 
# 4 5 6
# 7 8 9 

print("First element of first row:", new_arr[0][0])
print("Third element of second row:", new_arr[1][2])
print("Second element of third row:", new_arr[2][1])

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

# Searching in a Matrix Data Structure
def search_in_matrix(arr, x):
    #m=4, n=5
    for i in range(0,4):
        for j in range(0,5):
            if(arr[i][j]) == x:
                return 1
    return 

x = 9
search_arr = [[0, 6, 8, 9, 11],
       [20, 22, 28, 29, 31],
       [36, 38, 50, 61, 63],
       [64, 66, 100, 122, 128]]
if (search_in_matrix(search_arr, x)):
    print("YES")
else:
    print("NO")

# Sorting a Matrix Data Structure