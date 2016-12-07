//3. Given a non-negative int n,
//return the sum of its digits recursively (no loops).
// Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
//while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

function sumNumbers(number){
  if (number >= 0 && number < 10) {
      return number;
  } else {
    //console.log(number)
    return number % 10 + sumNumbers(Math.floor(number/10));
  }
}
var a = [1]
console.log(sumNumbers(322132))
console.log(a.lfdsfjfdsfdsfsdfkopdskfdspkfodspfkopdskfposdkfposdkjiddjiodijsfjiodsjiofdjiosfjiewoijiuoewjdweodjweodjoewpdjoeiwqjdoiqewpjdoiwqejdoiqewjodiewqjdoiweqkjdoidijowqoijdeqwukrkk9weqvgfdgfdgfdgfdgdfgdsifjldsk)
