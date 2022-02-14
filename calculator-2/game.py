"""A number-guessing game."""

import random

name = input("What is your name? ")
print(f"Hello {name}!")

def guessing_game():
    random_number = random.randint(1,10)

    guess = 0
    number_of_guesses = 1

    while guess != random_number:
        guess = input("What is your guess between 1 to 10? ")
        try:
            guess = int(guess)
            if guess > 10 or guess <0:
                print("Your guess is out of range. Try again.")
            elif guess > random_number:
                print("Your guess is too high. Try again.")
                number_of_guesses += 1
            elif guess < random_number:
                print("Your guess is too low. Try again.")
                number_of_guesses += 1
            else:
                print(f"You guessed correctly! It took you {number_of_guesses} guesses.")
        except ValueError:
            print("This is not a number, try again.")
    return number_of_guesses


def the_game():
    game_score = []
    i = True
    while i == True:
        play_game = input("Do you want to play a game?\n 1 = Yes\n 2 = no\nYour choice? ")
        try:
            play_game = int(play_game)
            if int(play_game) == 1:
               y = guessing_game()
               game_score.append(y)
            elif int(play_game) == 2:
                i = False
                print("Thanks for playing")
            else:
                print("This is not a valid option. Try again")
        except ValueError:
            print("This is not a valid option. Try again")
    return game_score


def best_score(the_game):
    lowest_score = min(the_game())
    return lowest_score

print(best_score(the_game))

