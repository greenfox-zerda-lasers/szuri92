'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods

var Stack = function () {

  this.stuffs = [];
  this.size = function() {
    sizeCounter = 0;
    for(i in this.stuffs) {
      sizeCounter += 1;
    }
    return sizeCounter;
  };

  this.push = function(element) {
    this.stuff += [element];
  };

  this.pop = function () {
    myLength = this.size();
    newArr = [];
    lastElem = this.stuffs[myLength-1];
      for(var i = 0; i < myLength-1; i++) {
            newArr += [this.stuffs[i]];
          }
        this.stuffs = newArr;
        return lastElem;
  };
}

var myStack = new Stack();
myStack.push('cica');
console.log(myStack.stuffs);
