#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) { console.error(error); } else {
    const data = JSON.parse(body);
    const moviesWithWedge = data.results.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(moviesWithWedge.length);
  }
});
