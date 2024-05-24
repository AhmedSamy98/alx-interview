#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api';
const filmID = process.argv[2];

if (process.argv.length > 2) {
  request(`${URL}/films/${filmID}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const cURLs = JSON.parse(body).characters;
    const cNames = cURLs.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, cReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(cReqBody).name);
        });
      }));

    Promise.all(cNames)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
