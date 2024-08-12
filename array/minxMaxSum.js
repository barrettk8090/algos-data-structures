//PROBLEM - Min Max Sum
// Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

// Example
// arr = [1,3,5,7,9]


// The minimum sum is 1+3+5+7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints

// Option 1: 
//  -- Get the 4 lowest values in the array & 4 highest values in the array
//  -- Sum each of those and save them to variables.
//  -- Print each of those values separated by a space 

// Option 2:
// -- Sum all possible variations of the array and save them to a dictionary
// -- Loop thru the dict and find the highest and lowest values in the dict 
// -- Print the highest and lowest values 

const minMaxSum = (arr) => {
    // Get the max value in the array
    let maxVal = Math.max(...arr)
    // Get the min value in the array 
    let minVal = Math.min(...arr)
    // Get the total of all values summed from the array
    let sum = arr.reduce((total, amount) => total + amount)
    console.log((sum - maxVal) + " " + (sum - minVal))

}

minMaxSum([1,3,5,7,9])