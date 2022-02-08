"""Simple Akamai ABCK challenge parser"""
from os import system
from challenge import Challenge

class Parser:
    """ABCK Parser class"""
    def __init__(self) -> None:
        self.headers = ["mn_al", "mn_tcl", "mn_il", "mn_lg"]
        self.logic()
        exit()


    def logic(self) -> None:
        """It's just logic of whole module making constructor more readable"""
        try:
            self.mode = int(input("Which mode do you want to use? \n[1 - one] [2 - compare] "))
        except ValueError:
            self.mode = 1

        if self.mode == 1:
            self.challenge = input("Paste bmak[mn_r] or whole sensor here: ").strip()
        else:
            self.challenge = (input("Paste whole sensor here: ").strip(),
                input("Paste bmak[mn_r] here: ").strip()
            )

        self.clear_console()

        if self.challenge != "":
            challanges_arr = []
            if isinstance(self.challenge, tuple):
                for item in self.challenge:
                    challanges_arr.append(Challenge(item))

            else:
                challanges_arr.append(Challenge(self.challenge))


    def clear_console(self) -> None:
        """Clears console"""
        system('cls')


    def compare_mode(self, changes: list) -> None:
        """Prints changes between two challenge strings"""
        print(changes)


Parser()
