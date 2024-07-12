// Given an array of integers, return a new array with each value doubled.
// For example:
// [1, 2, 3] --> [2, 4, 6]


function maps(arrayOfNumbers){
    const newArrayDoubled = [];
    
    for(let i = 0; i < arrayOfNumbers.length; i++) {
        const number = arrayOfNumbers[i] * 2;
        newArrayDoubled.push(number)
    }

    return newArrayDoubled;
}


console.log(maps([1, 2, 3])) // [2, 4, 6]
