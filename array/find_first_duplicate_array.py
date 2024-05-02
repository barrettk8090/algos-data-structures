# Given an Array, find the first duplicate value that occurs. If there are no duplicates, return -1.

# Input: [2, 1, 3, 3, 2]
# Output: 3

# Input: [1, 2, 3, 4]
# Output: -1

#Solution 1 - O(n^2), worst case scenario 

def find_first_dupe(arr):
    checker_arr = []
    length = len(arr)
    for i in arr:
        if i in checker_arr:
            length -= 1
            print(i)
            return i 
        elif i not in checker_arr and length > 1:
            checker_arr.append(i)
            length -= 1
        else:
            print(-1)
            return -1

find_first_dupe([2, 1, 3, 3, 2])
find_first_dupe([1, 2, 3, 4])
find_first_dupe([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
find_first_dupe([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,24])

# Solution 2 - O(n) - using POINTERS 

def find_first_dupe_pointers(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] == arr[right]:
            return arr[left]
        elif arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return -1

print(find_first_dupe_pointers([2, 1, 3, 3, 2])) 
print(find_first_dupe_pointers([1, 2, 3, 4]))  

# Solution 3 - O(n) - using SET()
def find_first_dupe_set(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1

# Example usage
print(find_first_dupe_set([2, 1, 3, 3, 2]))  
print(find_first_dupe_set([1, 2, 3, 4]))  


