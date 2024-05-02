# Find the nth element in the Fibonacci series. The Fibonacci sequence starts with a 0 followed by a 1. After that, every value is the sum of the two values preceding it. Here are the first seven values as an example: 0, 1, 1, 2, 3, 5, 8.

# Input: 0
# Output: 0

# Input: 2
# Output: 1

# Input: 10
# Output: 55
# Note that we are using zero-indexing for the series.

def fibonacci(nth_element):
    first_num = 0
    second_num = 1
    if nth_element == 0:
        return first_num
    elif nth_element == 1:
        return second_num
    elif nth_element > 1:
        list = [0, 1]
        for i, j in list:
            i + j 


    pass

# 0 + 1 = 1
# 1 + 1 = 2
# 2 + 1 = 3
# 3 + 2 = 5
# 5 + 3 = 8
# (previous number + even_more previous number)