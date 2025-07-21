#!/usr/bin/node
/* A recursive function that calculates the factorial of a number */

const number = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(number));
