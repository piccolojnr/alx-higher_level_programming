#!/usr/bin/node
const args = [];

process.argv.forEach(function (val, index, array) {
  if (!isNaN(val) && !args.includes(val)) { args.push(val); }
});
args.sort(function (a, b) {
  return b - a;
});

if (args.length < 2) {
  console.log(0);
} else { console.log(args[1]); }
