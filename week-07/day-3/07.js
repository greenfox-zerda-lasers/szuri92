'use strict';

var numbers = [2, , 11, 29, 67280421310721];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isPrimeArray(arr) {

    function itsPrime(number) {
    for( var j = 2; j < number; j++ ) {
      if( number % j === 0 ) {
        return false;
      }
    }
    return true;
  }
  return arr.every(itsPrime)
}

console.log(isPrimeArray(numbers));
