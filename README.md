# Hangman

Hangman is a Python terminal game, which runs in a mock terminal on Heroku.

Hangman is a traditional wordgame in which users are given an unknown, randomly selected word and will attempt to solve the word without losing all their lives. 

In the tradintional hangman style, users are given visual cues which will show how close the man is to hanging. 

[View the live project here](https://hangmangamedonald-e8eff857df0e.herokuapp.com/)


## User Experience (UX)

 - As a user, I want to be able to play the traditional wordgame hangman.
 - As a user, I want to be to myself and select from a variety of difficulty levels.
 - As a user, I want to be able to see how close I am to solving the word.
 - As a user, I want to be able to see how close I am from losing the game. 
 - As a user, I want to be able to store my high score.


## Features

### Opening Monologue

When the user starts the game, they are greeted with an openinig monologue. 

![This is a screen shot of the opening monologue](./assets/screenshots/opening_monologue.png)

## Enter your username
After the opening monolgue, users will be asked to enter their username. 
This user name is then stored for use later on when updating the scores to an external API


## Choosing the difficulty

After the opening monologue, the user will be asked to select the difficulty they would like to play. 

![This is a screenshot of the difficulty selection](./assets/screenshots/difficulty_choice.png)

Difficulty choices

EASY
- If the user selects "easy", they will be move on to play with randomly selected words with four letters or less

MEDIUM
- If the user selects "medium", they will move on to play  with randomly selected words with 7 letters or less

HARD
- If the user selects "hard", they will move on to play  with randomly selected words with 10 letters or less


Users have been given this difficulty choice so they can feel like they are being challenged, not only against themsleves but also against others who play. 


## Letter Selection

Following on from the difficulty selection, The user will be prompted to start guessing letters. Presented before the user input, is the unknown random word that has been blanked out. This gives the user an indiction of how many letters are in the word. 

![This is a screen shot of the letter selection](./assets/screenshots/letter_choice.png)


## Correctly guessed letters

Once the user has input their choice, they will receive feedback on whether or not the letter they have guessed is correct. 

![This is a screenshot of a correctly guessed letter](./assets/screenshots/correct_letter.png)

If the user has guessed correctly, They are presented with a message stating that they have guessed correctly. The correct letter replaces the blank space and the classic hangman drawing is displayed along with how many lives they have remaining. From here the user will be prompted for their next guess. 


## Incorrectly guessed letters

If the user has guessed incorrectly, They will be presented with a message stating what letter they got wrong and that it is not not in the randomly selected word. 

![this is a screenshot of an incorrectly guessed letter](./assets/screenshots/wrong_letter_five.png)

The user will also see displayed a list with the incorrectly guessed letter so they now know not to use this letter in their remaining attempts. 

The hangman image is displayed with its first body part and another message stating how many lives the user has remaining. 

From here the user is prompted to make their next attempt. 

If the user keeps guessing incorrectly, The same messages and images will be display until they lose all their lives. 

![This is a screen shot of 4 lives remaining](./assets/screenshots/wrong_letter_four.png)

![This is a screen shot of 3 lives remaining](./assets/screenshots/wrong_letter_three.png)

![This is a screen shot of 2 lives remaining](./assets/screenshots/wrong_letter_two.png)

![This is a screen shot of 1 lives remaining](./assets/screenshots/wrong_letter_one.png)

## Losing the Game

 - If the user gets the stage in the game where they have incorrectly guessed letters, that they lose all their lives, the game will end.

![This is a screenshot of game over](./assets/screenshots/wrong_letter_game_over.png)

- The user will be presented with a message stating that they have lost all their lives and the game is over.
- The user will also be presented with the completed word they were trying to guess 
- The final image of the hangman with all its body parts is displayed. 


## Winning the Game

- When the user has been able to guess all the correct letters in the random word, they will have won the game.

![This is a screenshot of the the user winnin the game](./assets/screenshots/winning_the_game.png)

- The terminal will diplay all the blank letters completed with a message to notify the user that they have guesed all the correct letters and the completed word is displayed. 


## Accumulating Points

- Classic Hangman is a fairly straightforward game to play and depending on each individual user, can be played and completed relatively quickly. 
- To give the user a reason to keep playing after they have solved a word and staying engaged, a scoring system has been implemented to the game.

![This is a screenshot of a user being awarded 1 point](./assets/screenshots/one_point.png)

- On completion of a word, the user will be awarded a point and asked to input if they wish to play again. 

- If the user inputs "yes", another word will be randomly selected with a fresh set of lives and the hangman image starts at the beginning. 

![This is a screenshot of a user scoring a second point](./assets/screenshots/score_two.png)

- This will continue until the user decides to end the game or until they lose all their lives on an attemped solve. 

## Storing points

- Upon a user voluntarily ending the game or losing the game, they will then be prompted to input their name. 

![This is a screenshot of the user prompt to enter their name](./assets/screenshots/two_points.png)

- Once their name is entered into the terminal, Their name and highscore will be posted into a google sheets document via an API. 

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

