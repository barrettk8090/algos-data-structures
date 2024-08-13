// 12:00:00AM = 00:00:00
// 01:00:00AM = 01:00:00
// …
// 11:59:00AM = 11:59:00

// 12:00:00PM = 12:00:00
// 01:00:00PM = 13:00:00
// …
// 11:59:00PM = 23:59:00

// If 12AM, return 00:00:00
// If 1AM - 11AM, return 1:00:00 - 11:00:00

// If 12PM, return 12:00:00
// If 1PM - 11PM, return current time + 12 


function timeConversion(s){
    // Get the first two digits
    let hourDigits = s.slice(0,2)
    // Get min/sec without AM/PM
    let minSec = s.slice(2,8)
    // Get AM or PM
    let timeOfDay = s.slice(-2)
    
    if (timeOfDay === "AM" && hourDigits === "12"){
        console.log(("00" + minSec).toString())
    } else if (timeOfDay === "AM" && hourDigits !== "12"){
        console.log((hourDigits + minSec).toString())
    } else if (timeOfDay === "PM" && hourDigits === "12") {
        console.log((hourDigits + minSec).toString())
    } else if (timeOfDay === "PM" && hourDigits !== "12"){
        console.log((parseInt(hourDigits) + 12).toString() + minSec.toString()) 
    }
}

timeConversion('02:27:03PM')
