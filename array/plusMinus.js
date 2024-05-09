//PROBLEM - PlusMinus

// Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

// Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

// Example

// arr = [1,1,0,-1,-1]

// There are  elements, two positive, two negative and one zero. Their ratios are 2/5, 2/5 and 1/5. Results are printed as:

// 0.400000
// 0.400000
// 0.200000


// Solution - O(n) 
// - n is the length of the input array; this is because the function iterates trhough each element of the array exactly once using a for ... of loop. Operations within the loop are constant time operations. 

function plusMinus(arr) {
    // Get length of the array to serve as denominator
    const length = arr.length;
    let pos_total = 0;
    let neg_total = 0;
    let zero_total = 0;
    //loop thru array for all nums & check pos, neg, or 0.
    for (let num of arr){
        if (num >= 1){
            pos_total += 1;
        } else if (num <= -1){
            neg_total += 1;
        } else {
            zero_total += 1;
        }
    }
    console.log((pos_total/length).toFixed(6));
    console.log((neg_total/length).toFixed(6));
    console.log((zero_total/length).toFixed(6));
}


plusMinus([1,1,0,-1,-1])