# Find the largest element in an array

#Basic loop - O(n)
def LargestInArray(arr):
    largest = 0
    for i in arr:
        if i > largest:
            largest = i
    return largest

print(LargestInArray([12,19,64,1,101,14,11,9,2]))

# Can use the built in max method - O(n)

arr = [12,19,64,1,101,14,11,9,2]

print(max(arr))