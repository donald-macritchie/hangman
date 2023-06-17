import gspread
from google.oauth2.service_account import Credentials
from hangman_words import words
import random
from hangman_images import hangman_lives
from difficulty import game_difficulty, generate_word, validate_input

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman_scores')


username = ""
user_score = 0


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


def check_if_game_over(lives_remaining, game_over, computer_choice):
    """
    checks if the user has run out of lives,
    if so, the game is over.
    """
    if lives_remaining == 0:
        game_over = True
        print("You have lost all your lives, Game Over!\n")
        print(f"The word you were looking for was: {computer_choice}")
    return game_over


def play_game(computer_choice, user_score):
    """
    Loops through the randomly selected word with each guess the user makes.
    Sets a condition for the completed word, i.e., all blanks removed.
    Prints ASCII art to the terminal based on the user's input.
    """

    game_over = False
    lives_remaining = 6
    wrong_letter = []
    blanks = hide_word(computer_choice)

    while not game_over:
        print(blanks)
        input_valid = False
        while not input_valid:
            try:
                user_choice = input("Please guess a letter: ").lower()
                if not user_choice.isalpha():
                    raise ValueError("Only letters are valid, please try again")
                input_valid = True
            except ValueError as e:
                print(str(e))

        checked_user_choice = check_user_choice(computer_choice,
                                                user_choice, blanks)
        if not checked_user_choice:
            wrong_letter = incorrect_letter(user_choice, wrong_letter)
            lives_remaining -= 1
            game_over = check_if_game_over(lives_remaining, game_over, computer_choice)
        else:
            blanks = checked_user_choice
            print(f"You chose {user_choice}, That is correct!")

        print(blanks)

        if "_" not in blanks:
            game_over = True
            print("You have guessed all the correct letters!")
            print(f"The completed word is '{computer_choice}'.")
            user_score += 1

        print(hangman_lives[lives_remaining])

        if lives_remaining != 0:
            print(f"You have {lives_remaining} lives remaining\n")

    update_highscores(user_score)
    return user_score


def play_again(user_score):
    """
    allows user to play game again, looping
    back to play_game()
    """
    end_game = False
    while end_game is False:
        is_input_valid = False
        while is_input_valid is False:
            print("Would you like to play again?")
            continue_game = input("Type 'Yes' or 'No': ").lower()
            is_input_valid = validate_input(continue_game,
                                            ['yes', 'no', 'y', 'n'])
            if is_input_valid is False:
                print("Invalid input, please enter 'yes' or 'no'.")
        if continue_game == "yes":
            print("Here is your next word:\n")
            computer_choice = generate_word(difficulty)
            user_score = play_game(computer_choice, user_score)
        elif continue_game == "no":
            print("Thanks for playing. Game over")
            end_game = True
    return user_score


def get_username():
    """
    Asks for the users username and
     check if it is valid
     """
    is_valid = False
    while is_valid is False:
        username = input("Please enter your username: ")
        if len(username) >= 3:
            is_valid = True
        else:
            print("Enter at least three letters.")
    return username


def update_highscores(final_score):
    """
    Takes user's name and score and updates the
    google sheet with the new data
    """

    print(f"Thanks for playing {username}, your score is {final_score}\n")
    print("Updating highscore worksheet... \n")
    # users name is appended to googlesheet
    high_score_worksheet = SHEET.worksheet("highest_score")
    if difficulty == "easy":
        high_score_worksheet.append_row([username, final_score, " ", " "])
    elif difficulty == "medium":
        high_score_worksheet.append_row([username, " ", final_score, " "])
    elif difficulty == "hard":
        high_score_worksheet.append_row([username, " ", " ", final_score])

    print("Highest scores worksheet updated successfully.\n")


def main():
    """
    Runs the core game functionality
    """
    user_score = 0
    user_score = play_game(computer_choice, user_score)
    play_again(user_score)


if __name__ == "__main__":
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")
    username = get_username()
    [computer_choice, difficulty] = game_difficulty()
    main()
