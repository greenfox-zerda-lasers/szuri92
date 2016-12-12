'use strict';

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b) {
  this.a = a;
  this.b = b;
}

Rectangle.prototype.getArea = function() {
  return this.b * this.a;
}

Rectangle.prototype.getCircumference = function() {
  return 2*this.a + 2*this.b;
}
var rec1 = new Rectangle(2, 30);
var square = new Rectangle(5, 5);
console.log(square.getArea());
console.log(square.getCircumference());
console.log(rec1.getArea());
console.log(rec1.getCircumference());
