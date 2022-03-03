function submitProfile(evt) {
  evt.preventDefault();

  const data = {
    name: document.querySelector('#name-field').value,
    age: document.querySelector('#age-field').value,
    occupation: document.querySelector('#occupation-field').value,
    // salary: document.querySelector('salary option = checked'),
    // education: document.querySelector('#name-field').value,
    state: document.querySelector('#state-field').value,
    // city_type: document.querySelector('#state-field').value,
    // garden: document.querySelector('#state-field').value,
    // tv_watch: document.querySelector('#state-field').value,

    // fill in the rest
  };
  // console.log(data);

  fetch('/api/profile', {
    "method": 'POST',
    "body": JSON.stringify(data),
    "headers": {
      'Content-Type':'application/json',
    },
  })
  .then(response => response.json())
  .then(responseJson => {
    document.querySelector("#profiles").insertAdjacentHTML('beforeend', `<div class="box"> ${responseJson.fullname},${responseJson.age},${responseJson.occupation}</div>`);
  });
  

  // make request to server to get the data
  // add the data the server returns to the document
  // (you can add it to the end of the div with ID "profiles")
}

document.querySelector('#profile-form').addEventListener('submit', submitProfile);
