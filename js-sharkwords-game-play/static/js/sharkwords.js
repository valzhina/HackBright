const ALPHABET = 'abcdefghijklmnopqrstuvwxyz';
const WORDS = [
  'strawberry',
  'orange',
  'apple',
  'banana',
  'pineapple',
  'kiwi',
  'peach',
  'pecan',
  'eggplant',
  'durian',
  'peanut',
  'chocolate',
];

let numWrong = 0;

// Loop over the chars in `word` and create divs.
//

const createDivsForChars = (word) => {
  //Looking for section containers in HTML//
  const wordContainer = document.querySelector('#word-container');
  for (let letter of word) {
    wordContainer.insertAdjacentHTML('beforeend', `<div class="letter-box ${letter}"></div>`);
  }
};

// Loop over each letter in `ALPHABET` and generate buttons.
//
const generateLetterButtons = () => {
  const letterButtonContainer = document.querySelector('#letter-buttons');
  for (const char of ALPHABET) {
    letterButtonContainer.insertAdjacentHTML('beforeend', `<button>${char}</button>`);
  }
};

// Set the `disabled` property of `buttonEl` to `true.
//
// `buttonEl` is an `HTMLElement` object.
//
const disableLetterButton = buttonEl => {
  buttonEl.disabled = true;
};

// Return `true` if `letter` is in the word.
//
const isLetterInWord = letter => document.querySelector(`div.${letter}`) !== null;

// Called when `letter` is in word. Update contents of divs with `letter`.
//
const handleCorrectGuess = letter => {
  if (isLetterInWord(letter)) {
    const letters = document.querySelectorAll(`div.${letter}`);
    for (let theLetter of letters){
      theLetter.innerHTML = `${letter}`;
    }
  }
};
/* <div class="letter-box h"> h</div>
<div class="letter-box h"> h</div> */
//
// Called when `letter` is not in word.
//
// Increment `numWrong` and update the shark image.
// If the shark gets the person (5 wrong guesses), disable
// all buttons and show the "play again" message.

const handleWrongGuess = () => {
  numWrong += 1;
  if (numWrong === 5) {
    for (const button of document.querySelectorAll("button")) {
      disableLetterButton(button);
    }

    const hiddenLink = document.querySelector("#play-again");
    hiddenLink.preventDefault();

  } else {
      return numWrong;
  }
};

//  Reset game state. Called before restarting the game.
const resetGame = () => {
  window.location = '/sharkwords';
};

// This is like if __name__ == '__main__' in Python
//
(function startGame() {
  // For now, we'll hardcode the word that the user has to guess.
  const word = 'hello';

  createDivsForChars(word);
  generateLetterButtons();

  for (const button of document.querySelectorAll("button")) {
    // add an event handler to handle clicking on a letter button
    button.addEventListener('click', (evt) => {
      const letter = button.innerHTML;
      disableLetterButton(button);
      if (isLetterInWord(letter)) {
        handleCorrectGuess(letter);
      }
      else {
        handleWrongGuess();
      }
    });
  }

  // add an event handler to handle clicking on the Play Again button
  // YOUR CODE HERE
})();

// let dog_name = ourDog.name
// console.log(dog_name)

// ourDog.name = "Keesah"