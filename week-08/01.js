'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(sound) {
  this.sound = sound;
}

Animal.prototype.say = function() {
  console.log(this.sound);
}

var dog = new Animal('woof');
var cat = new Animal('meow');
var 

dog.say();
cat.say();
