#!/usr/bin/node
// prints all characters of a Star Wars movie:
const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function printCharacters (characterData, idx) {
  request(characterData[idx], (characterError, characterResponse, characterBody) => {
    if (characterError) {
      console.error(characterResponse.message);
    } else {
      console.log(JSON.parse(characterBody).name);
      if (idx + 1 < characterData.length) {
        printCharacters(characterData, idx + 1);
      }
    }
  });
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    const data = JSON.parse(body);
    const characterData = data.characters;
    printCharacters(characterData, 0);
  }
});
