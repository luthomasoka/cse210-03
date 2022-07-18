class Jumper:

    def __init__(self):
        self.jumper_name = ""
        self.wins = 0
        self.losses = 0

    def get_jumper_name(self):
        self.jumper_name = input("Please enter your name: ")

    def get_result(self, result):
        if result == "W":
            self.wins += 1
        elif result == "L":
            self.losses += 1

    def display_result(self):
        print(f"\nJumper: {self.jumper_name} has {self.wins} wins and {self.losses} losses")