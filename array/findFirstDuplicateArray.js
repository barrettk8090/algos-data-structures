// Find first dupe Worst Case

const findFirstDupeWC = (arr) => {
    let checker_arr = []
    length = arr.length - 1
    i = 0
    debugger;
    for (let item of arr) {
       if (checker_arr.includes(item)){
        console.log(item);
        return item;
       } else {
        checker_arr.push(item);
       }
    }
    console.log(-1)
    return -1;
}

// findFirstDupeWC([2, 1, 3, 3, 2])

//Find first dupe with Pointers - NOTE: This is incorrect, because in theory we want to find the first dupe from left to right. This starts on both ends and works inwards, so it sees that 2 and 2 === so it returns 2. 

const findFirstDupePointers = (arr) => {
    let left = 0;
    let right = arr.length -1;

    debugger;
    while (left < right){
        if (arr[left] === arr[right]){
            return arr[left];
        } else if (arr[left] < arr[right]){
            left += 1;
        } else {
            right -=1
        }
    }
    return -1
}

console.log(findFirstDupePointers([2,1,3,3,2]))