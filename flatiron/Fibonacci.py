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

### Solution 1 - While Loop – O(n)

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

### Solution 2 – Memoization – 0(n)
# The recursive solution to the Fibonacci problem can be optimized using memoization. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again. This significantly reduces the time complexity from exponential to linear.
# Time Complexity: O(n). The memoization technique ensures that each Fibonacci number is computed only once, thus reducing the number of redundant calculations. The time complexity is linear because each number up to n is computed exactly once.

cache = {0: 0, 1: 1}

def fibonacci_memoized(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return cache[n]

print(fibonacci_memoized(10))

### Solution 3 – Iterative Solution - 0(n)
# An iterative solution to the Fibonacci problem uses a loop to calculate the Fibonacci sequence. This approach avoids the overhead of recursive calls and is generally faster for large inputs.
# Time Complexity: O(n). The iterative solution has a linear time complexity because it performs a single pass through the sequence to calculate the nth Fibonacci number.

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(10))