#!/usr/bin/node
/* checks if command line argument(s) was passed to the script */
const argument = process.argv;
/* removed name of executable and path to node interpreter */
argument.shift();
argument.shift();

if (argument.length === 0) {
  console.log('No argument');
} else if (argument.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
