from dictionary import Dictionary
from jumper import Jumper
class Enquirer:

    def __init__(self):
        self.word = ""
        self.letter = ""
        self.parachute_points = 5
        self.guessed_letters = []
        self.missing_letters = ""
        self.guess = ""
        self.error = 0
        self.keep_playing = True
        self.finish = ""     # W = wins     L = lose

    def request_letter(self):
        self.guess = input("\nType a letter ")
        self.guess = self.guess.strip().lower()
        return self.guess

    def letters_length(self):
        return ["_" for self.letter in self.word]

    def compare_letters(self):
        self.guessed_letters = self.letters_length(self.word)

    def mark_right_guess(self):
        index = 0
        no_letter=0
        for self.letter in self.word:
            if (self.guess == self.letter):
                self.guessed_letters[index] = self.letter
                no_letter = 1
            index += 1
        if no_letter == 0:
            self.error += 1

    def start_game(self):
        word = Dictionary()
        player = Jumper()
        player.get_jumper_name()
        self.word = word.words()
        self.letters = self.letters_length()
        self.guessed_letters = self.letters_length()
        self.parachute()
        print(f"\n", self.letters_length())
        while self.keep_playing:
            self.request_letter()
            self.mark_right_guess()
            self.check_match()
        return self.finish

    def check_match(self):
        self.missing_letters = self.guessed_letters.count('_')
        if(self.missing_letters) == 0:
            print(f"\nCongratulations!! You guessed the secret word: {self.word.upper()}")
            self.keep_playing = False
            self.finish = "W"
        else:
            print("")
            print(self.guessed_letters)
            print('\nYou still need to guess {} letter(s)'.format(self.missing_letters))
            print('You still have {} tries'.format(5-self.error))
            self.parachute()
            if self.error == 5:
                self.keep_playing = False
                self.finish = "L"
                print(f"\nThe secret word is: {self.word.upper()}")
        pass

    def parachute(self):
        if self.error == 0:
            print("")
            print(" ___ ")
            print("/___\ ")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 1:
            print("")
            print("/___\ ")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 2:
            print("")
            print("\   /")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 3:
            print("")
            print(" \ /")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 4:
            print("")
            print("  0")
            print(" /|\ ")
            print(" / \ ")
        elif self.error == 5:
            print("")
            print("  x")
            print(" /|\ ")
            print(" / \ ")
        pass