'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rocket(consumption){
  this.consumption = consumption;
  this.tank = 0;
}

Rocket.prototype.fill = function(fill){
  this.tank += fill;
}

Rocket.prototype.launch = function() {
  if (this.tank >= this.consumption) {
    console.log('Launch successful');
    this.tank -= this.consumption;
  } else {
    console.log('Not enogh fuel to launch');
  }
}

var alpha1 = new Rocket(5);
var alpha2 = new Rocket(10);
alpha1.fill(20);
console.log(alpha1.tank);
console.log(alpha2.tank);
alpha2.launch();
alpha1.launch();
console.log(alpha1.tank);
