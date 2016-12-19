'use strict';
// create a function that returns it's input factorial
function calculateFactorial(number){
  if (number <= 1) {
    return 1;
  } else {
    return number * calculateFactorial(number-1)
  }
}

module.exports = calculateFactorial;
