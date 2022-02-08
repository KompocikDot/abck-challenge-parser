"""Challenge object containing headers, methods and original input"""
from colorama import Fore


class Challenge:
    """Challenge object"""
    def __init__(self, user_input: str) -> None:
        self.passed_str = user_input
        self.headers = ["mn_al", "mn_tcl", "mn_il", "mn_lg"]
        self.mnlg_headers = [
            "mn_abck", "mn_rts", "mn_psn", "mn_cc", "mn_cd",
            "mn_cd + mn_mc_indx", "rand_toString(16)", "mn_cc + rand_toString(16)",
            "mn_s(r)", "mn_rt", "mn_wt", "get_cf_date()",
        ]

        self.detect_sensor()
        self.destruct_str()
        self.print_deconstructed()


    def detect_sensor(self) -> None:
        """Method to detect whether user passed challenge or whole sensor"""
        try:
            self.passed_str = self.passed_str.split("-94,-124,")[1].split("-1,2,-94,-126")[0]
            self.whole_akam = True
        except IndexError:
            self.whole_akam = False

    def destruct_str(self) -> None:
        """Destructs challenge into smaller pieces"""
        self.deconstructed = self.passed_str.split(";")[:4]
        self.deconstructed_mnlg = self.deconstructed[-1].split(",")
        self.deconstructed_mnlg = self.deconstructed_mnlg[:8] + \
            [",".join(self.deconstructed_mnlg[8:-3])] + self.deconstructed_mnlg[-3:]
        self.deconstructed_mnlg = zip(self.mnlg_headers, self.deconstructed_mnlg)
        self.deconstructed = zip(self.headers, self.deconstructed)

    def print_deconstructed(self) -> None:
        """Pretty prints deconstructed challenge"""
        for item in self.deconstructed:
            print(Fore.CYAN + item[0] + Fore.RESET + ": " + item[1])

        print(Fore.GREEN + "mn_lg ingredients" + Fore.RESET)
        for mnlg_item in self.deconstructed_mnlg:
            print(Fore.CYAN + mnlg_item[0] + Fore.RESET + ": " + mnlg_item[1])
