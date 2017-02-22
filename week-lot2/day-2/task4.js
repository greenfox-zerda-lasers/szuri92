//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

const number = 100;

function getSum() {
  let sum = 0;
  for(let i = 1; i <= number; i++) {
    sum += i;
  }
  return sum;
}

function getSquareofSum() {
  return Math.pow(getSum(), 2);
}

function getSumofSquares() {
  let sum = 0;
  for (let i = 1; i <= number; i++) {
    sum += Math.pow(i, 2);
  }
  return sum;
}

function getDef() {
  return getSquareofSum() - getSumofSquares();
}

console.log(getSumofSquares());
console.log(getDef());
