'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function each(myArr, fun) {

  myArr.forEach(function(item, index) {
    fun(index, item);
  });
}

var anArray = [1, 2, 3, 4, 5, 6, 7, 8]

each(anArray, console.log)
