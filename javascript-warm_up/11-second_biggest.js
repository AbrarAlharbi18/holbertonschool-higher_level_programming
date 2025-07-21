#!/usr/bin/node
/* sorts a list of command line arguments */

const arg = process.argv;

// removes the path to the executable and path to node interpreter
const number = arg.slice(2);
const parse = function (element) {
  return parseInt(element);
};
const compare = function (a, b) {
  return b - a;
};
if (number.length < 2) {
  console.log('0');
} else {
  const newNumber = number.map(parse);
  newNumber.sort(compare);
  console.log(newNumber[1]);
}
