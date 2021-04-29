# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"
ALREADY_GUESSED = "You've guessed that letter before!"
LETTER_NOT_FOUND = "This letter wasn't in the word - try again!"
LETTER_FOUND = "You found a letter!"
WRONG_WORD = "That isn't the right word!"

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.word = word
        self.status = STATUS_ONGOING
        self.guessed_letters = set()

    def guess(self, char):
        if char in self.guessed_letters:
            self.remaining_guesses -= 1
        return Hangman.ALREADY_GUESSED
        self.remaining_guesses -= 1
        return self.guessed_letters.add(char)
            
        if char not in self.word:
            if self.attempts == 0:
                return Hangman.STATUS_LOSE
            return Hangman.LETTER_NOT_FOUND
        if "_" not in self.get_masked_word:
            return Hangman.STATUS_WIN
        return Hangman.LETTER_FOUND

    def get_masked_word(self):
        result = ""
        for char in self.word:
            if char in self.guessed_letters:
                result += char
            else:
                result += "_"
        return result

    def guess_word(self, word):
        self.attempts -= 1
        if word == self.word:
            return Hangman.STATUS_WON
        return Hangman.WRONG_WORD
       
    

class User:
    SUCCESS = "Input accepted succesfully"
    INVALID_LETTER_LENGTH = "Letter must have exactly 1 character"
    LETTER_NOT_ALPHA = "Letter must be an alphabetic character"
    INVALID_GUESS_TYPE = "The guess type must be either 1 (letter) or 2 (word)"
    LETTER_ALREADY_GUESSED = "You already guessed that letter"
    UNKNOWN_CATEGORY = "The specified category is unknown"
    NOT_YES_NO = "That wasn't 'yes' or 'no'"
    INPUT_NO = 1

    def _get_user_input(self, prompt, validator=lambda x: User.SUCCESS):
        while True:
            user_input = input(prompt).lower()
            is_valid = validator(user_input)
            if is_valid is not User.SUCCESS:
                print("Input accepted")
            else:
                return user_input


    def _get_category_prompt(self, header, options, underline="="):
        prompt = "\n".join([header, underline*len(header)])
        options = "\n".join(["\t".format(category) for category in options])
        return "\n".join([prompt, options])

   

    def get_word_to_guess(self):
        prompt = self._get_category_prompt("Categories:", self.options)
        def is_valid_category(category):
            if category not in self.options: return User.UNKNOWN_CATEGORY
            return User.SUCCESS
        return random.choice(self.options[self._get_user_input(prompt, is_valid_category)])
        


    def get_letter_guess(self):
        def is_valid_letter(char):
            if len(letter) != 1: return User.INVALID_LETTER_LENGTH
            if not letter.isalpha(): return User.LETTER_NOT_ALPHA
            if self.game.letter_already_guessed(letter): return User.LETTER_ALREADY_GUESSED

            return User.SUCCESS

        return self._get_user_input("What letter would you like to guess? ",
                                is_valid_letter)

    def get_guess_type(self):
        def is_valid_guess(guess_type):
            if guess_type not in [1, 2]: return User.INVALID_GUESS_TYPE
            return User.SUCCESS

        return self._get_user_input("Enter 1 to guess a letter, or 2 to guess the word")
    
    def repeat(self):
        def is_yes_no(yn):
            if yn[0].lower() in ["y", "n"]: return User.SUCCESS
            return User.NOT_YES_NO
        return self._get_user_input("Play again (Y/N)?", is_yes_no)



class HangmanDriver:

    def __init__(self, options=None):
        self.options = options or {"Artists" : ["Beyonce", "Rihanna", "Wale", "6lack"]}
        self.game = None


     
    def get_status(self):
        print("Current status: {}".format(self.get_masked_word))
        print(graphics[self.game.remaining_guesses])


    def loop(self):
        while True:
            word = self.get_word_to_guess()
            self.game = Hangman(word)
            while True:
                self.display_status()
                guess_type = self.get_guess_type()
                if guess_type == 1:
                    letter = self.get_letter_guess()
                    guess_result = self.game.guess(char)
                elif guess_type == 2:
                    word = self.get_word_guess()
                    guess_result = self.game.guess_word(word)

                print(Hangman.result_messages[guess_result])
                if guess_result == Hangman.STATUS_WIN:
                    break
            play_again = self.repeat()
            if play_again[0].lower() == "n": break


if __name__ == '__main__':
    HangmanDriver().loop()
