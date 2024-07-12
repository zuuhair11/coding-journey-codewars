// Create a function which answers the question 'Are you playing banjo?'.
// If your name starts with the letter 'R' or lower case 'r', you are playing banjo!
// The function takes a name as its only argument, and returns one of the following strings:
function areYouPlayingBanjo(name) {
    // Implement me
    if(name.at(0).toLowerCase() === 'r') {
        return `${name} plays banjo`;
    }

    return `${name} does not play banjo`;
}


console.log(areYouPlayingBanjo('Adam'))     // Adam does not play banjo
console.log(areYouPlayingBanjo('Ringo'))    // Ringo plays banjo
