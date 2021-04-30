import random
import string
from words import words

def get_valid_word(words):

    word = random.choice(words)
    while "-" or " " in word:
        word = random.choice(words)
        return word

def Hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 10

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have", lives, "lives left and you've used these letters: ", " ".join(used_letter))

        # what current word is
        word_list = [letter if letter in used_letter else "-" for letter in word]
        print("Current word:"," ".join(word_list))
        user_letter = input("Please enter a letter: ").upper()
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1
                print("Letter not in word")

        elif user_letter in used_letter:
            print("You already guessed that letter. Try again.")
        else:
            print("You typed an invalid character. Try again")
    if lives == 0:
        print("Sorry you died. The word was: ", word)
    
    else:
        print("You got it!! ", word)

Hangman()