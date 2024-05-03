import time
import random

# Sort an Array of numbers using selection sort. The selection sort algorithm sorts an array by repeatedly finding the minimum element (lowest value) in the input Array, and then putting it at the correct location in the sorted Array.

# Input: [3, -1, 5, 2]
# Output: [-1, 2, 3, 5]
# You ARE allowed to use a built-in array method to find the minimum value—you need not recreate it algorithmically. Feel free to try it out for an extra challenge, though.

# For this task, we are also asking you to calculate the average runtime of your solution. In other words, you run it a bunch of times and then divide the total time it took for the solution to run by the number of times it ran.

# Here is the pseudocode for creating your own basic benchmarking procedure:

        # store the current time in a variable called start time

        #   loop 1000 times:
        #   execute the method using a small input, e.g. three items if input is an Array
        #   execute the method using a larger input, e.g. 100 items if input is an Array

# average runtime = (current time - start time) / 2000

## Solution 1A - O(n^2) 
def selection_sort(arr):
    new_arr = []
    while len(arr) > 0:
        new_arr.append(min(arr))
        arr.pop(arr.index(min(arr)))
    print(new_arr)

## SOLUTION 1B - Calculating time. 
# Benchmarking
start_time = time.time()

# Run the function 1000 times with small input
for _ in range(1000):
    selection_sort([random.randint(-100, 100) for _ in range(3)])

# Run the function 1000 times with large input
for _ in range(1000):
    selection_sort([random.randint(-100, 100) for _ in range(100)])

end_time = time.time()

# Calculate average runtime
average_runtime = (end_time - start_time) / 2000
print(f"Average runtime: {average_runtime} seconds")

selection_sort([3, -1, 5, 2])

######################################################