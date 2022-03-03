'use strict';

// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // Select the button
  // const button = document.querySelector('#get-fortune-button');
  // button.addEventListener('click', () => {

  fetch('/fortune')
    .then(response => response.text())
    .then(responseData => document.querySelector('#fortune-text').innerHTML = responseData);
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();

  // Because we need to send data to the server, and it's a GET request
  // => we need to create a query string and pass the link to fetch
  // https://google.com/search?city=San+Francisco

  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;
  const queryString = new URLSearchParams({"zipcode" : zipcode}).toString(); // "zipcode" : 94544
  const urlQueryString = url + "?" + queryString; // /weather.json?zipcode=94544

  // TODO: request weather with that URL and show the forecast in #weather-info
  fetch(urlQueryString)
    .then(response => response.json())
    .then(responseData => {
      console.log(responseData);
      document.querySelector("#weather-info").innerHTML = responseData.forecast; //type on forecast
    })
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS

function orderMelons(evt) {
  evt.preventDefault();

  // Form first
  const formInputs = { // keys have to match keys in python file
    "melon_type": document.querySelector('#melon-type-field').value,
    "qty": document.querySelector('#qty-field').value,
  };
  console.log(formInputs);

  // fetch Post Request
  fetch('/order-melons.json', {
    "method": 'POST',
    "body": JSON.stringify(formInputs),
    "headers": {
      'Content-Type':'application/json',
    },
  })
    .then(response => response.json())
    .then(responseJson => {
      document.querySelector("#order-status").innerHTML = responseJson.msg;
      if (responseJson.code === 'ERROR') {
        document.querySelector("#order-status").classList.add('order-error');
      }
    })
  // creat error message red text of #order-status div
  
  // TODO: show the result message after your form
  // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}
document.querySelector('#order-form').addEventListener('submit', orderMelons);
