import gspread
from google.oauth2.service_account import Credentials
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


# Create function for game
# create function to have latest scores input into google sheet
# create function to have highest scores input into google sheet

# print("Welcome to Hangman!\n")
# print("Guess the letters to complete the word")
# print("Try to guess the word in the least amount of guesses")
# print("Dont let the man hang!\n")
user_score = 0


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


def play_game(computer_choice):
    game_over = False
    lives_remaining = 6
    wrong_letter = []
    blanks = hide_word(computer_choice)


#     def correct_letters():
#         for position in range(len(computer_choice)):
#             letter = computer_choice[position]
#   #           if user_choice ==#  letter:
#                 blanks[p# osition] = letter
#                 pri# nt(f"You chose {user_choice}, Tha# t is correct!")

#     def incorrect_letter():
#         lives_remainin# g = 6
#         if user_choice not in computer_choice:
#             print(f"You guessed {user_choice}, This le# tter#  is not in the word.")
#   #           print("Try again\n")
#             wrong_let# ter(# )
#             lives_remain# ing -= 1
#             if # live# s_remaining == 0:
#  #  #     #           game_over = True
#    #              print("You have lost all your lives, Game Over\n")
#                 print(f"The word you were looking for was: {computer_choice}")
#         return computer_choice

    while game_over is False:
        user_choice = input("Please guess a letter: ")
        checked_user_choice = check_user_choice(computer_choice, user_choice,
        blanks)
        if checked_user_choice is False:
            print(f"You guessed {user_choice}, This letter is not in the word")
            print("Try again\n")
            wrong_letter.append(user_choice)
            print(f"Incorrect letter: {wrong_letter}")
            lives_remaining -= 1
            if lives_remaining == 0:
                game_over = True
                print("You have lost all your lives, Game Over!\n")
                print(f"The word you were looking for was: {computer_choice}")
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
            # user_score += 1
            print(f"Your score is {user_score}")



# def play_again():
#     """
#     Asks the user to play again if they complete the word
#     """
#     game_over = True
#     continue_game = input("play again y/n?: ")
#     if continue_game == 'y':
#         play_game(computer_choice)
#         game_over = False


# def score(user_score):
#     """
#     Keeps track of the user score
#     """
    
#     user_score += 1
#     print(f"You have a score of {score}")
#     while score >= 0:
#         play_again()


def main():
    # game_difficulty()
    play_game(computer_choice)
    # score(user_score)


if __name__ == "__main__":
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")
    [computer_choice, difficulty] = game_difficulty()
    print(computer_choice)
    # user_score = 0
    main()

