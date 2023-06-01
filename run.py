import gspread
from google.oauth2.service_account import Credentials
from hangman_words import words
import random
from hangman_images import hangman_lives
from difficulty import game_difficulty

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('hangman_scores')


# Create function for game
# create function to have latest scores input into google sheet
# create function to have highest scores input into google sheet

def play_game():
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")

    game_over = False
    lives_remaining = 6
    wrong_letter = []

    computer_choice = random.choice(words)
    print(computer_choice)

    blanks = []
    for letter in range(len(computer_choice)):
        blanks += "_"
    print(blanks)

    while not game_over:
        user_choice = input("Please guess a letter: ")

        for position in range(len(computer_choice)):
            letter = computer_choice[position]
            if user_choice == letter:
                blanks[position] = letter
                print(f"You chose {user_choice}, That is correct!")

        print(blanks)

        if user_choice not in computer_choice:
            print(f"You guessed {user_choice}, This leter is not in the word.")
            print("Try again\n")
            wrong_letter.append(user_choice)
            print(f"Incorrect letters: {wrong_letter}")
            lives_remaining -= 1
            if lives_remaining == 0:
                game_over = True
                print("You have lost all your lives, Game Over\n")
                print(f"The word you were looking for was: {computer_choice}")

        if "_" not in blanks:
            game_over = True
            print("You have guessed all the correct letter!")

        print(hangman_lives[lives_remaining])

        if lives_remaining != 0:
            print(f"You have {lives_remaining} lives remaining \n")



def main():
    play_game()


main()