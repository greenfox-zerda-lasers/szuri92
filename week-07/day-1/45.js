'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function myShortestString(string){
  var min = string[0].length+1;
  var result = '';
  for (var i = 0; i < string.length; i++) {
    if (string[i].length < min) {
        min = string[i].length;
        result = string[i];
    }
  }
  return result;
}



console.log(myShortestString(names))
console.log(names[0].length)
