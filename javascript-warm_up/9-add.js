#!/usr/bin/node
/* A function that adds to numbers from command line arguments */

const firstNumber = parseInt(process.argv[2]);
const secondNumber = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(firstNumber, secondNumber);
