# Instructions
# Given an Array of strings, return the shortest string. If there is more than one string of that length, return the string that comes first in the list. The Array will have a minimum length of 1.

        # Input: ['aaa', 'a', 'bb', 'ccc']
        # Output: 'a'

        # Input: ['cat', 'hi', 'dog', 'an']
        # Output: 'hi'

        # Input: ['flower', 'juniper', 'lily', 'dandelion']
        # Output: 'lily'

# Solution 1 - Using .sort(key=len) – sort is O(n log n) where n is # of elements in list

def find_shortest_string(arr):
    arr.sort(key=len)
    print(arr[0])

find_shortest_string(['aaa', 'a', 'bb', 'ccc'])
find_shortest_string(['cat', 'hi', 'dog', 'an'])
find_shortest_string(['flower', 'juniper', 'lily', 'dandelion'])

# Solution 2 - O(n) where n is the number of elements in the array 
def shortest_string(arr):
    if not arr:
        return None
    
    min_length = len(arr[0]) # Start by setting min_length to first element in array
    min_str = arr[0]
    
    for i in range(1, len(arr)):
        if len(arr[i]) < min_length: # Checking each item in the list to see if its less than arr[0]
            min_length = len(arr[i])
            min_str = arr[i]
    
    return min_str

# Solution 3 - Using the built in min() method with key of length - O(n)
def find_shortest_string_min(arr):
    print(min(arr, key=len))

find_shortest_string_min(['aaa', 'a', 'bb', 'ccc'])
find_shortest_string_min(['cat', 'hi', 'dog', 'an'])