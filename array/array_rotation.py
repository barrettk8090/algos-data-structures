# Array Rotation: 
# https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/?ref=lbp 
# Given an array like: [1,2,3,4,5,6,7]
# Rotate to the following: [2,3,4,5,6,7,1]  /// Left rotation by 1 


# SOLUTION 1 - O(log10)

# First function to reverse the given array by swapping the 
# first and last numbers 
def reverse(start, end, arr):
    # Number of iterations needed for reversing the list
    no_of_reverse = end-start+1

    #By incrementing count value, swapping of first and last elements is done 
    count = 0
    while ((no_of_reverse)//2 != count):
        arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
        count +=1  
    return arr 

# Second function takes array, length of array, and no of rotations as input
def left_rotate_array(arr, size, d): 
    #Reverse the entire list
    start = 0
    end = size-1
    arr = reverse(start, end, arr)

    # Divide the array into two sub-arrays based on the no of rotations
    # Divide the first sub-array, reverse the first sub-array

    start = 0
    end = size-d-1
    arr = reverse(start, end, arr)

    # Divide the second sub-array
    # Reverse the second sub-array
    start = size-d
    end - size-1
    arr = reverse(start, end, arr)
    return arr 

arr = [1,2,3,4,5,6,7,8]
size = 8
d = 1
print("Original array: ", arr)

# Finding all the symmetric rotation number
if (d <= size):
    print("Rotated array ", left_rotate_array(arr, size, d))
else:
    d = d % size
    print("Rotated array: ", left_rotate_array(arr, size, d))

############################################################

# SOLUTION 2 - Rotate using a temp array - O(n)

# rotate the array by "d" elements
def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0 
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr 

arr = [1,2,3,4,5,6,7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
