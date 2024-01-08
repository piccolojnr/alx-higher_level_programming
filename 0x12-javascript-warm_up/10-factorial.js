#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  let x = parseInt(process.argv[2]);
  for (let i = x - 1; i >= 1; i--) {
    x = x * i;
  }
  console.log(x);
}
