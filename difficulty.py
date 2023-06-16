from hangman_words import words
import random


def generate_word(user_difficulty):
    """
    Generates a randomly selected word based on
    the users choice in game_difficulty().
    The random word is returned to the main game in run.py
    """
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


def validate_input(input, valid_choices):
    if input.lower() in valid_choices:
        return True
    else:
        return False



def game_difficulty():
    """
    Asks the user to input their difficulty level,
    their response is then passed into the generate_word() function
    """
    print("Choose your difficulty level!\n")
    print("EASY - Words with 4 letters or less")
    print("MEDIUM - Words with 7 letters or less")
    print("HARD - Words with 10 letters or less\n")
    print("Please select a difficulty.")
    input_valid = False
    while input_valid is False:
        user_difficulty = input("Type: 'easy', 'medium' or 'hard': \n").lower()
        input_valid = validate_input(user_difficulty, ["easy", "medium", "hard"])
        if input_valid is False:
            print("Invalid difficulty choice, please try again.\n")
    return [generate_word(user_difficulty), user_difficulty]
