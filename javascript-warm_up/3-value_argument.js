#!/usr/bin/node
/* A script that prints the first argument passed to it */

const arg = process.argv;
// removed the path to executable and path to node interpreter
arg.shift();
arg.shift();
if (arg[0] === undefined) {
  console.log('No argument');
} else {
  console.log(arg[0]);
}
