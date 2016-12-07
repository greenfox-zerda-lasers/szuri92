
//1. write a recursive function
//that takes one parameter: n
//and counts down from n



function countDown(number){
  if(number < 1) {
    return 0;
  } else {
    console.log(number)
    return countDown(number-1);
  }
}

console.log(countDown(2313))
