#!/usr/bin/node
if (isNaN(process.argv[1])) {
  console.log('Missing size');
} else {
  const arg1 = parseInt(process.argv[1]);
  for (let i = 0; i < arg1; i++) {
    console.log('X'.repeat(arg1));
  }
}
