#!/usr/bin/node
const myDict = require('./101-data').dict;

const entries = Object.entries(myDict);
const vals = entries.map(entry => entry[1]);
const uniqVals = [...new Set(vals)];

const newDict = {};

for (const val of uniqVals) {
  const ls = [];
  for (const entry of entries) {
    if (entry[1] === val) {
      ls.push(entry[0]);
    }
  }
  newDict[val] = ls;
}

console.log(newDict);
