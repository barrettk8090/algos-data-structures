# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

################################################

# First Solution - O(n^2)

def twoSum(nums, target):
    # First, we iterate over the indices of nums. range(len(nums)) generates a list of indices from 0 to len(nums) - 1.
    for i in range(len(nums)):
        # Then, we iterate over the indices of nums again. This time, we start from i + 1 to avoid using the same element twice.
        for j in range(i+1, len(nums)):
            # If the sum of the two elements at indices i and j is equal to the target, we return the indices as a list.
            if nums[i] + nums[j] == target:
                return [i, j] 
            
# Second Solution - O(n): Creating a dictionary to store the elements we have seen so far.

def twoSum(nums, target):
    # Create an empty dictionary to store the elements we have seen so far.
    num_dict = {}
    # We iterate over the indices and elements of nums using the enumerate function.
    for i, num in enumerate(nums):
        # We calculate the complement of the current element by subtracting it from the target.
        complement = target - num
        # If the complement is in the dictionary, we return the indices of the complement and the current element.
        if complement in num_dict:
            return [num_dict[complement], i]
        # Otherwise, we add the current element to the dictionary with its index as the value.
        num_dict[num] = i

# enumerate(nums) takes the list nums and gives you a special kind of iterator. This iterator doesn't just give you the numbers, it gives you pairs of numbers and their positions. So, for the list [2, 7, 11, 15], it would give you pairs like (0, 2), (1, 7), (2, 11), and (3, 15). The first number in each pair is the position of the item in the list, and the second number is the item itself.