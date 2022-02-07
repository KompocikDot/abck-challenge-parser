"""Simple Akamai ABCK challenge parser"""
from os import system
from colorama import Fore

class Parser:
    """ABCK Parser class"""
    def __init__(self) -> None:
        self.headers = ["mn_al", "mn_tcl", "mn_il", "mn_lg"]
        self.logic()


    def logic(self) -> None:
        """It's just logic of whole module making constructor more readable"""
        try:
            self.mode = int(input("Which mode do you want to use? \n[1 - one] [2 - compare] "))
        except ValueError:
            self.mode = 1

        if self.mode == 1:
            self.challenge = input("Paste bmak[mn_r] here: ").strip()
        else:
            self.challenge = (input("Paste bmak[mn_r] here: ").strip(),
                input("Paste bmak[mn_r] here: ").strip()
            )

        if self.challenge != "":
            if isinstance(self.challenge, tuple):
                changes = []
                for challenge_str in self.challenge:
                    changes.append(self.undo_mnpr(challenge_str))
                self.compare_mode(changes)

            else:
                self.undo_mnpr(self.challenge)


    def clear_console(self) -> None:
        """Clears console"""
        system('cls')


    def undo_mnpr(self, abck_string: str) -> list[tuple] | None:
        """Destructs challenge string into smaller pieces"""
        mn_pr = self.challenge.split(";")
        self.clear_console()

        zipped = zip(self.headers, mn_pr)
        if self.mode == 2:
            return zipped

        for zipped_item in zipped:
            print(Fore.BLUE + f"{zipped_item[0]}" + Fore.RESET, f": {zipped_item[1]}")

    def compare_mode(self, changes: list) -> None:
        """Prints changes between two challenge strings"""
        print(changes)

    def check_mnlg(self) -> None:
        pass

Parser()
