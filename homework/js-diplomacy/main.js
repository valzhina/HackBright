'use strict';

/** ***** Functions & event handlers ****** */

function changeColor() {
    const colorChangeEls = document.querySelectorAll('.color-change');
  
    for (const el of colorChangeEls) {
      el.classList.add('red');
    }
  }
  
  function validateNumber(evt) {
    evt.preventDefault();
  
    const numberInput = document.querySelector('#number-input');
    const userNum = Number(numberInput.value); // typecast to num
  
    const formFeedback = document.querySelector('#formFeedback');
    if (isNaN(userNum) || userNum >= 10) {
      formFeedback.innerText = 'Please enter a smaller number';
    } else {
      formFeedback.innerText = 'You are good to go!';
    }
  }
  
  /** ***** Attach event handlers ****** */
  
  document.querySelector('.color-changer').addEventListener('click', changeColor);
  document.querySelector('.number-form').addEventListener('submit', validateNumber);