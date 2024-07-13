// In this kata the aim is to compare each pair of integers from 
// two arrays, and return a new array of large numbers.
// Note: Both arrays have the same dimensions.
'use strict';

function getLargerNumbers(a, b) {
    const newArray = [];
    for(let i = 0; i < a.length; i++) {
        newArray[i] = Math.max(a[i], b[i]);
    }

    return newArray;
}


let arr1 = [13, 64, 15, 17, 88];
let arr2 = [23, 14, 53, 17, 80];
console.log(getLargerNumbers(arr1, arr2)); // Returns [23, 64, 53, 17, 88]
