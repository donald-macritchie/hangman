from hangman_words import words


def easy():
    [word for word in words if len(word) <= 4]
    print("You have selected the EASY level\n")


def medium():
    [word for word in words if len(word) <= 7]
    print("You have selected the MEDIUM level\n")


def hard():
    [word for word in words if len(word) <= 10]
    print("You have selected the HARD level\n")


def game_difficulty():
    print("Choose your difficulty level!\n")
    print("EASY - Words with 4 letters or less")
    print("MEDIUM - Words with 7 letters or less")
    print("HARD - Words with 10 letters or less\n")
    print("Please select a difficulty.")

    user_difficulty = input("Type: 'easy', 'medium' or 'hard': ").lower()
    if user_difficulty == "easy":
        easy()
    elif user_difficulty == 'medium':
        medium()
    elif user_difficulty == 'hard':
        hard()

    if user_difficulty != 'easy' and 'medium' and 'hard':
        print("Invalid difficulty choice, please try again.\n")
        game_difficulty()
