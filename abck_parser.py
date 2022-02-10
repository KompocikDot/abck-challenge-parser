"""Simple Akamai ABCK challenge parser"""
from os import system
from challenge import Challenge


class Parser:
    """ABCK Parser class"""
    def __init__(self) -> None:
        self.logic()


    def logic(self) -> None:
        """It's just logic of whole module making constructor more readable"""
        try:
            pick = int(input("1 - Parser \n2 - Documentation \nPick an option: "))
        except ValueError:
            pick = 1

        if pick == 1:
            self.challenge = input("Paste bmak[mn_r] or whole sensor here: ").strip()
            system('cls')

            if self.challenge != "":
                Challenge(self.challenge)

        else:
            print("""abck-challenge parser by KompocikDot

to run parser select option 1 and paste data in format: 
sensor_data or (example) 0.da349878396a,0.90387bcba3432,0.83853cb5af7ca [...] 1644305170741;  
parser will print red values if 

mn_cc: not equal to mn_abck + mn_rts + mn_psn 
m = mn_cd + mn_mc_indx: not equal mn_cd + 0 
mn_cc + m + n: not equal to mn_cc + m + n
mn_s(r): length of string.split(",") other than 32
get_cf_date(): value smaller than mn_rts or not len is different than 13 
other values are not checked atm""")
