#!/usr/bin/node
/* prints C is fun based on the first command line argument passed */

const arg = process.argv;
const result = parseInt(arg[2]);
let string;
if (isNaN(result)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < result; i++) {
    string = '';
    for (let i = 0; i < result; i++) {
      string += 'X';
    }
    console.log(string);
  }
}
