#!/usr/bin/node
/* prints C is fun based on the first command line argument passed */

const arg = process.argv;
const result = parseInt(arg[2]);
if (isNaN(result)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < result; i++) {
    console.log('C is fun');
  }
}
