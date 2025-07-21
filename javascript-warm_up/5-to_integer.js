#!/usr/bin/node
/* converting the first command line argument to a number */

const arg = process.argv;
// removing the path to the executable and path to node interpreter
arg.shift();
arg.shift();

const result = parseInt(arg[0]);
if (isNaN(result)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${result}`);
}
