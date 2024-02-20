#!/usr/bin/node
// computes the number of tasks completed by user id.
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    const data = JSON.parse(body);
    const usersWithCompletedTasks = data.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(usersWithCompletedTasks);
  }
});
