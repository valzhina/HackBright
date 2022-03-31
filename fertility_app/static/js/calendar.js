// Create Date object via Date object constructor function
// it will return the current date and time + specifies the browser timezone as a fulltext string
const date = new Date();
// date.setMonth(8);
// const month = date.getMonth();
// date.setDate(7);
// console.log(date);

//Main function to render the Calendar
const fertilityCalendar = () => {

    const monthDays = document.querySelector(".days");

    // Create new Date object and this time define current year and current month. 0 will specify the last day of previous month, +1, 0: end day of this month
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    // console.log(lastDay);

    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

    // console.log(date.getDay());

    //getDay returns the index number of the days of the week. Sun index number  = 0
    // Get index of first day of month
    const firstDayIndex = new Date(date.getFullYear(), date.getMonth(), 1).getDay();
    // console.log(firstDayIndex)

    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

    //console.log(lastDayIndex());

    const nextDays = 7 - lastDayIndex - 1;

    const months = [
        "January",
        "February",
        "March",
        "April", 
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November", 
        "December",
    ];

    // Select h1(month) element in date class and change it property, by using Data object method .getMonth 
    document.querySelector('.date h1').innerHTML = months[date.getMonth()];
    document.querySelector('.date p').innerHTML = new Date().toDateString();

    let days = "";

    // x will be the counter, then define the number of iterations, and on each iteration create a new div 
    // on each iteration a new div element will be created for the previouse month day. Define the condition where x > 0
    for(let x = firstDayIndex; x > 0; x--){
        days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
    }

    for(let i = 1; i <= lastDay; i++){
        if(i === new Date().getDate() && date.getMonth() === new Date().getMonth()) {
            days += `<div id="${i}" class="today day selected_date">${i}</div>`;
        }
        else{
            // create a div element and pass i vairable  
            days += `<div class="day" id="${i}" >${i}</div>`;
        }
    }
    // monthDays.innerHTML = days;

    for(let j = 1; j <= nextDays; j++){
        days += `<div class="next-date">${j}</div>`;
    }

    monthDays.innerHTML = days;
    
    const dayElements = document.querySelectorAll('.day');  

    for (let day of dayElements) {
        day.addEventListener('click',() => {

            if (document.querySelector(".selected_date") !== null) {
                document.querySelector(".selected_date").classList.remove("selected_date");
            }

            day.classList.add("selected_date");
        });

        day.addEventListener('dblclick',() => {
            console.log(day.id);
            // document.getElementById("exampleModal").modal('show');;
            // day.classList.add("first_period_date");
            addNote(day);
            console.log(day.id);
        });
    }
}

document.querySelector('.prev').addEventListener('click',() => {
    date.setMonth(date.getMonth() -1);
    fertilityCalendar();
});

document.querySelector('.next').addEventListener('click',() => {
    date.setMonth(date.getMonth() + 1);
    fertilityCalendar();
});

fertilityCalendar();


function addPeriod(evt) {
    evt.preventDefault();

    const formInputs = {
        "period_start": document.querySelector('#').value,
        "period_length": document.querySelector('#length').value,
    };
    console.log(formInputs);
    fetch('/add_period.json', {
        "method": 'POST',
        "body": JSON.stringify(formInputs),
        "headers": {
          'Content-Type':'application/json',
        },
    });
}

document.querySelector("#reg-modal-period-form").addEventListener("click", addPeriod);


function addNote(evt) {
    evt.preventDefault();
    
    if (document.querySelector(".selected_date").id !== null) {
        let day = document.querySelector(".selected_date").id;
        const dtt = new Date(date.getFullYear(), date.getMonth(), day);

        let note = document.querySelector("#note_text").value;

        const formInputs = {
            "date_time": dtt,
            "note_text": document.querySelector('#note_text').value,
        };

        fetch('add_note.json', {
            "method": 'POST',
            "body": JSON.stringify(formInputs),
            "headers": {
            'Content-Type':'application/json',
            },
        });
    }
    else {
        console.log("select day");
    }
}

document.querySelector("#reg-modal-note-form").addEventListener("click", addNote);



// function getPeriodInfo(day) {
    
//     const input = new FormData();
//     input.append('day', day)
    
//     fetch("/period_form", {
//         method: 'POST',
//         body: input,
//     })
//     .then(response => response.json())
//     .then(document.querySelector("#img_list").innerHTML="")
//     .then(responseJson => {
//         for(let i in responseJson.img) {
//             document.querySelector("#img_list").insertAdjacentHTML('afterbegin',`<p>${responseJson.meal_type[i]}</p><img src="${responseJson.img[i]}"><p>${responseJson.ingredient[i]}</p>`);
//         }
//     })