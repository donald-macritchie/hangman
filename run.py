import gspread
from google.oauth2.service_account import Credentials
from hangman_words import words
import random
from hangman_images import hangman_lives
from difficulty import game_difficulty, generate_word

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_scores')


def hide_word(computer_choice):
    """
    Will take the randomly generated word from generate_word()
    in difficulty.py and replace each letter with an underscore,
    so the user can only see how many letters are in the word.
    """

    blanks = []
    for letter in range(len(computer_choice)):
        blanks += "_"
    return blanks


def check_user_choice(computer_choice, user_choice, blanks):
    """
    Checks if the users guess is in the randomly selected word.
    """
    if user_choice not in computer_choice:
        return False
    if user_choice in computer_choice:
        for index, letter in enumerate(computer_choice):
            if letter == user_choice:
                blanks[index] = letter
        return blanks


def incorrect_letter(user_choice, wrong_letter):
    """
    If an incorrect guess has been made,
    the wrong letter will be appended to a new list
    and displayed to the user
    """
    print(f"You guessed {user_choice}, This letter is not in the word.")
    print("Try again\n")
    wrong_letter.append(user_choice)
    print(f"Incorrect letters: {wrong_letter}")
    return wrong_letter


def check_if_game_over(lives_remaining, game_over):
    """
    checks if the user has run out of lives,
    if so, the game is over.
    """
    if lives_remaining == 0:
        game_over = True
        print("You have lost all your lives, Game Over!\n")
        print(f"The word you were looking for was: {computer_choice}")
    return game_over


def play_game(computer_choice):
    """
    loops through the randomly selected word with each guessthe user makes.
    sets condition for the completed word, ie all blanks removed.
    prints ascii art to the terminal based on users input.

    """
    game_over = False
    lives_remaining = 6
    wrong_letter = []
    blanks = hide_word(computer_choice)

    while game_over is False:
        print(blanks)
        user_choice = input("Please guess a letter: ").lower()
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
            print(f"The completed word is '{computer_choice}'.")

        print(hangman_lives[lives_remaining])

        if lives_remaining != 0:
            print(f"You have {lives_remaining} lives remaining \n")


def play_again(user_score):
    """
    allows user to play game again, looping
    back to play_game()
    """
    end_game = False
    while end_game is False:
        user_score += 1
        print(f"Your current score is {user_score} words")
        continue_game = input("Would you like to play again? Type 'Yes' or 'No':").lower()
        if continue_game == "yes":
            computer_choice = generate_word(difficulty)
            print(computer_choice)
            play_game(computer_choice)
        elif continue_game == "no":
            print(f"Your high score is {user_score} words")
            print("Thanks for playing. Game over")
            end_game = True
        return user_score



def update_highscores():
    """
    Takes user's name and score and updates the
    google sheet with the new data
    """
    final_score = 1
    # User enters their name
    name = input("Please enter your name: ")
    print(f"Thanks for playing {name}, your highscore is {final_score}\n")
    print("Updating highscore worksheet... \n")
    # users name is appended to googlesheet
    high_score_worksheet = SHEET.worksheet("highest_score")
    high_score_worksheet.append_row([name, " ", " ", final_score])
    # if user_level == "easy":
    #     high_score_worksheet.append_row([name, final_score, " ", " "])
    # elif user_level == "medium":
    #     high_score_worksheet.append_row([name, " ", final_score, " "])
    # elif user_level == "hard":
    #     high_score_worksheet.append_row([name, " ", " ", final_score])

    # Users difficulty is identified

    # Users score is appended to difficulty column

    # print("Highest scores worksheet updated successfully.\n")


def main():
    # play_game(computer_choice)
    # play_again(user_score)
    update_highscores()


if __name__ == "__main__":
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")
    [computer_choice, difficulty] = game_difficulty()
    print(computer_choice)
    user_score = 0
    main()