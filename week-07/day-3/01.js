'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"
function writeMynumber(number) {

  var numberString = ['zero', 'one', 'two', 'three', 'four', 'five', 'many'];
  if (number <= 5 && number > 0) {
    for(var i = 0; i < numberString.length; i++){
      if (i === number) {
        return numberString[i];
      }
    }
  } else {
    return numberString[6]
  }
}


console.log(writeMynumber(4))
