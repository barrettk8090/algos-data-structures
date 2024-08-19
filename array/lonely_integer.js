//  O(n log(n))
function lonelyInteger(a) {
    a.sort();
    
    for (let i = 0; i < a.length; i += 2) {
        if (a[i] !== a[i + 1]) {
            console.log(a[i])
            return a[i];
        }
    }
    console.log(a[a.length - 1]);
    return a[a.length - 1];
}

lonelyInteger([1,2,3,4,3,2,1])

