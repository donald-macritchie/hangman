from hangman_words import words


def easy():
    easy_word = [word for word in words if len(word) <= 4]
    print("You have selected the EASY level\n")


def medium():
    medium_word = [word for word in words if len(word) <= 7]
    print("You have selected the MEDIUM level\n")


def hard():
    hard_word = [word for word in words if len(word) <= 10]
    print("You have selected the HARD level\n")

