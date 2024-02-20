#!/usr/bin/node
// A script that reads and prints the content of a file
const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', function (error, data) {
  if (error) { console.error(error); } else { console.log(data); }
});
