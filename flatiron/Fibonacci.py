# Find the nth element in the Fibonacci series. The Fibonacci sequence starts with a 0 followed by a 1. After that, every value is the sum of the two values preceding it. Here are the first seven values as an example: 0, 1, 1, 2, 3, 5, 8.

# Input: 0
# Output: 0

# Input: 2
# Output: 1

# Input: 10
# Output: 55
# Note that we are using zero-indexing for the series.

#0th element = 0 
#First element = 0 
#Second element = 1 
#Third element = 1 
#Fourth element = 2
#Fifth element = 3
#Sixth element = 4

def fibonacci(nth_element):
    if nth_element == 0 or nth_element == 1:
        print(0)
        return 0
    elif nth_element == 2:
        print(1)
        return 1
    elif nth_element > 1:
        list = [0, 1]
        i = 0 
        j = 1 
        while nth_element >= len(list):
            new_value = list[i] + list[j]
            list.append(new_value)
            i += 1
            j += 1
        print(list[nth_element])
        

fibonacci(10)
