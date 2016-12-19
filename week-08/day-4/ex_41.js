function mySumm(list){
  var sum = 0;
  for(var i = 0; i < list.length; i++){
    sum += list[i];
  }
  return sum;
}

module.exports = mySumm;


console.log(mySumm([1, 2, 3, 'a', 4, 5]))
