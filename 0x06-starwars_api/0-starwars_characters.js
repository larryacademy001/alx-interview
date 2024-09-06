#!/usr/bin/node

const req = require('request');
const movieId = process.argv[2];
const api_url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req(api_url, async (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const characterId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      req(characterId, (err, response, body) => {
        if (err) {
          reject(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
