"""Simple Akamai ABCK challenge parser"""
from os import system
from challenge import Challenge

class Parser:
    """ABCK Parser class"""
    def __init__(self) -> None:
        self.headers = ["mn_al", "mn_tcl", "mn_il", "mn_lg"]
        self.logic()


    def logic(self) -> None:
        """It's just logic of whole module making constructor more readable"""

        self.challenge = input("Paste bmak[mn_r] or whole sensor here: ").strip()
        system('cls')

        if self.challenge != "":
            Challenge(self.challenge)
