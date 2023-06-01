import gspread
from google.oauth2.service_account import Credentials
from hangman_words import words

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

def play_game():
    print("Welcome to Hangman!\n")
    print("Guess the letters to complete the word")
    print("Try to guess the word in the least amount of guesses")
    print("Dont let the man hang!\n")


def main():
    play_game()
    print(words)


main()