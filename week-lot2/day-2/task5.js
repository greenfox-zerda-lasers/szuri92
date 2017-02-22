// What is the 10 001st prime number?

function isPrime(n) {
 if (isNaN(n) || !isFinite(n) || n%1 || n<2) {
   return false;
 }
 if (n%2==0) return (n==2);
 if (n%3==0) return (n==3);
 var m=Math.sqrt(n);
 for (var i=5;i<=m;i+=6) {
  if (n%i==0)     return false;
  if (n%(i+2)==0) return false;
 }
 return true;
}


function primeOf10001() {
  let counter = 0;
  let number = 0;
  while (counter < 10001) {
    if (isPrime(number) === true) {
      counter++;
    }
    number++ ;
  }
  return number - 1;
}

console.log(primeOf10001());
