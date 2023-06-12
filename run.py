# import gspread
# from google.oauth2.service_account import Credentials
from hangman_words import words
import random
from hangman_images import hangman_lives
from difficulty import game_difficulty, generate_word

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('hangman_scores')

def user_name():
    name = input("Please enter your name: ")
    return name


def hide_word(computer_choice):
    blanks = []
    for letter in range(len(computer_choice)):
        blanks += "_"
    return blanks


def check_user_choice(computer_choice, user_choice, blanks):
    if user_choice not in computer_choice:
        return False
    if user_choice in computer_choice:
        for index, letter in enumerate(computer_choice):
            if letter == user_choice:
                blanks[index] = letter
        return blanks


def incorrect_letter(user_choice, wrong_letter):
    print(f"You guessed {user_choice}, This letter is not in the word.")
    print("Try again\n")
    wrong_letter.append(user_choice)
    print(f"Incorrect letters: {wrong_letter}")
    return wrong_letter
   

def check_if_game_over(lives_remaining, game_over):
    if lives_remaining == 0:
        game_over = True
        print("You have lost all your lives, Game Over!\n")
        print(f"The word you were looking for was: {computer_choice}")
    return game_over


def play_game(computer_choice):
    game_over = False
    lives_remaining = 6
    wrong_letter = []
    blanks = hide_word(computer_choice)

    while game_over is False:
        user_choice = input("Please guess a letter: ")
        checked_user_choice = check_user_choice(computer_choice,
        user_choice, blanks)
        if checked_user_choice is False:
            wrong_letter = incorrect_letter(user_choice, wrong_letter)
            lives_remaining -= 1
            game_over = check_if_game_over(lives_remaining, game_over)
        else:
            blanks = checked_user_choice
            print(f"You chose {user_choice}, That is correct!")
            
        print(blanks)

        if "_" not in blanks:
            game_over = True
            print("You have guessed all the correct letter!")

        print(hangman_lives[lives_remaining])

        if lives_remaining != 0:
            print(f"You have {lives_remaining} lives remaining \n")



def play_again(user_score):
    end_game = False
    while end_game is False:
        user_score += 1
        print(f"Your current score is {user_score} words")
        continue_game = input("Would you like to play again? Type 'Yes' or 'No': ").lower()
        if continue_game == "yes":
            computer_choice = generate_word(difficulty)
            print(computer_choice)
            play_game(computer_choice)
        elif continue_game == "no":
            print(f"Your high score is {user_score} words")
            print("Thanks for playing. Game over")
            end_game = True
            



def main():
    play_game(computer_choice)
    return play_again(user_score)



if __name__ == "__main__":
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")
    user_name()
    [computer_choice, difficulty] = game_difficulty()
    print(computer_choice)
    user_score = 0
    main()

