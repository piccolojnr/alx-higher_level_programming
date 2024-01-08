#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const arg1 = process.argv[1];

const arg2 = process.argv[2];

console.log(add(+arg1, +arg2));
