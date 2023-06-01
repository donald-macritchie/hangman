import gspread
from google.oauth2.service_account import Credentials
from hangman_words import words
import random

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
                print("That is correct.")

        print(blanks)

        if user_choice not in computer_choice:
            lives_remaining -= 1
            if lives_remaining == 0:
                game_over = True
                print("You have lost all your lives, Game Over")

        if "_" not in blanks:
            game_over = True
            print("Game over")


def main():
    play_game()


main()