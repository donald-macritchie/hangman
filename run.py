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

def game_difficulty():
    print("Choose your difficulty level!\n")
    print("EASY - Words with 4 letters or less")
    print("MEDIUM - Words with 7 letters or less")
    print("HARD - Words with 10 letters or less\n")
    print("Please select a difficulty.")

    user_difficulty = input("Type: 'easy', 'medium' or 'hard': \n").lower()
    if user_difficulty == "easy":
        easy_words = [word for word in words if len(word) <= 4]
        computer_choice = random.choice(easy_words)
        return computer_choice
    elif user_difficulty == 'medium':
        medium_words = [word for word in words if len(word) <= 7]
        computer_choice = random.choice(medium_words)
        return computer_choice
    elif user_difficulty == 'hard':
        hard_words = [word for word in words if len(word) <= 10]
        computer_choice = random.choice(hard_words)
        return computer_choice
    elif user_difficulty != 'easy' and 'medium' and 'hard':
        print("Invalid difficulty choice, please try again.\n")
        game_difficulty()

        
print("Welcome to Hangman!\n")
print("Guess the letters to complete the word")
print("Try to guess the word in the least amount of guesses")
print("Dont let the man hang!\n")


computer_choice = game_difficulty()
print(computer_choice)


def play_game(computer_choice):
    game_over = False
    lives_remaining = 6
    wrong_letter = []

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


def play_again():
    """
    Asks the user to play again if they complete the word
    """
    continue_game = input("play again? y or n")
    if continue_game == "y":
        play_game(computer_choice)
    else:
        print("game over")


def score():
    """
    Keeps track of the user score
    """
    score = 0
    score += 1
    print(f"You have a score of {score}")
    while score >= 0:
        play_again()


def main():
    # game_difficulty()
    play_game(computer_choice)
    score()
    

main()