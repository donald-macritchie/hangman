from hangman_words import words

def easy():
    easy_word = [word for word in words if len(word) <= 4]
    print("You have selected the EASY level\n")

