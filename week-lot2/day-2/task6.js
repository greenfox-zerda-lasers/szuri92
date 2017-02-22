// What is the sum of the digits of the number 2^1000?
function sumOfPower(powered) {
  let sum = 0;
  let power = Math.pow(2, powered);
  for (let i = 0; i < power.toString().length; i++) {
    sum += parseInt(power.toString()[i]);
  }
  return sum;
}

function sumOfPower2(powered) {
  let sum = 0;
  let power = Math.pow(2, powered);
  let lastDigit;
  for(let i = 0; power >= 0; i++) {
    if (power < 10 && power > 0) {
      sum += power
      return sum;
    } else {
        lastDigit = power % 10;
        console.log(lastDigit);
        sum += lastDigit;
        power = Math.floor(power / 10);
    }
  }
  return sum;
}

console.log(sumOfPower2(1000));
