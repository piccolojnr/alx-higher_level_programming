#!/usr/bin/node
if (isNaN(process.argv[1])) {
  console.log('Missing number of occurrences');
} else {
  const arg1 = parseInt(process.argv[1]);
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
}
