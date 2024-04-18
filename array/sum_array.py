import functools

# Example inputs
# arr = [1, 2, 3]

# Loop solution - time complexity: O(n)
def SumArray(arr):
    total = 0
    for num in arr:
        total = total + num
    print(total)

SumArray([1,2,3])
SumArray([5,10,15,20])

# sum() solution - time complexity: 0(n)
arr = [5,10,15,20]
print(sum(arr))

# using .reduce() -- link: https://www.geeksforgeeks.org/reduce-in-python/ 
# .reduce(function, sequence) - received two arguments

lis = [1, 3, 5, 6, 2] 
print(functools.reduce(lambda a,b: a+b, lis))