from enquirer import Enquirer
from jumper import Jumper

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
       enquirer: is the one who verifies if the letters given by the jumper are in the word
    """

    def __init__ (self):
        self.enquirer = Enquirer()
        self.jumper = Jumper()
        self.result = ""
        self.continue_playing = True
        self.player_choice = ""

    def play_game(self):
        while self.continue_playing:
            self.scenario()
        self.jumper.get_result(self.result)
        self.player_choice = input("Play again? [y/n]: ").lower()

    def Determine_game_play(self):
        if self.player_choice == "y":
            self.continue_playing = True
        elif self.player_choice == "n":
            self.continue_playing = False
    
    def scenario (self):
        """
        """
        print("*********************************")
        print("***Welcome to Jumper Game***")
        print("*********************************")
        self.result = self.enquirer.start_game()
        self.end_game()
        self.jumper.display_result()

    def end_game(self):
        if self.result == "W":
            self.msg_win()
        else:
            self.msg_lose()

    def msg_lose(self):
        print("\033[91mGosh, you've been hanged!\n")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           \33[0;0m \n")

    def msg_win(self):
        print("\033[93mCongratulations, You Won!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       \33[0;0m \n")