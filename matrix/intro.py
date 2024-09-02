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