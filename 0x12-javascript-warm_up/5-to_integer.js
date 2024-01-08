#!/usr/bin/node
if (isNaN(process.argv[1])) {
  console.log('Not a number');
} else {
  if (process.argv[1]) {
    console.log('My number:', parseInt(process.argv[1]));
  } else {
    console.log('Not a number');
  }
}
