from hangman_words import words
import random

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
