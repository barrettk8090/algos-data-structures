# Given an Array of values, use recursion to find the target value. Return true if found, otherwise false.

# Input: [1, 2, 3], 2
# Output: true

# Input: [3, 2, 1], 4
# Output: false

#Slicing --> array[start:stop] | start - inclusive, stop - exclusive
#No start given, defaults to the beginning of the sequence
#No stop given, defaults to the end of the sequence

def rec_search(arr, target):
    # Checks if array is empty - upon recursion of all elements of array
    if len(arr) == 0:
        return False
    # Checks to see if the first element is in the array is target - recursion eventually checks all values at index 0
    if arr[0] == target:
        return True
    # If no conditions are met, calls method again with first element sliced thru to the end.
    # On each recursion, only arr[0] is called 
    # E.g. First: [1,2,3] | Second: [2,3] | Third: [3] | End: []
    return rec_search(arr[1:], target)

print(rec_search([1,2,3], 2))
print(rec_search([1,2,3,4,5,6,7,8,9], 10))
print(rec_search([1,2,3,4,5,6,7,8,9], 9))