#!/usr/bin/node
/* A function that is visible from outside */

const add = function (a, b) {
  return a + b;
};
module.exports = { add };
