
function getValues(evt) {
    evt.preventDefault();
    
    const req_date = document.querySelector("#date").value;
    const start_time = document.querySelector("#start_time").value;
    const end_time = document.querySelector("#end_time").value;
    console.log(req_date, start_time, end_time);

    const formInputs = {
        "req_date":req_date,
        "start_time":start_time,
        "end_time":end_time,
    };

    fetch("/schedule", {
        "method": 'POST',
        "body": JSON.stringify(formInputs),
        "headers": {
          'Content-Type':'application/json',
        },
    })
    .then(response => response.json())
    .then(responseJson => drawAvailable(responseJson.available));
}

function drawAvailable(times) {

    
    for (const t of times) {
        document.querySelector("#results").insertAdjacentHTML('beforeend', t);
    }



}

document.querySelector("#submit").addEventListener("click", getValues);
