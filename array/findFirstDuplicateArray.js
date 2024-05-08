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

findFirstDupeWC([2, 1, 3, 3, 2])