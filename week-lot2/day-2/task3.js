// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

var getResult = function () {
  let counter = 0;
  let number = 2520;
  while (counter < 20) {
    for (let i = 1; i < 21; i++) {
      if(counter >= 20) {
        return number;
      } else if (number % i === 0) {
        counter++;
      } else {
        counter = 0;
        number++;
      }
    }
  }
}

console.log(getResult());
