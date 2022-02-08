"""Challenge object containing headers, methods and original input"""
from colorama import Fore


class Challenge:
    """Challenge object"""
    def __init__(self, user_input: str) -> None:
        self.passed_str = user_input
        self.headers = ["mn_al", "mn_tcl", "mn_il", "mn_lg"]
        self.mnlg_headers = [
            "mn_abck", "mn_rts", "mn_psn", "mn_cc", "mn_cd",
            "m = mn_cd + mn_mc_indx", "n = rand_toString(16)", "mn_cc + m + n",
            "mn_s(r)", "mn_rt", "mn_wt", "get_cf_date()",
        ]

        self.detect_sensor()
        try:
            self.destruct_str()
            self.check_mnlg()
            self.print_deconstructed()
        except NonSensorException:
            print("Invalid challenge string passed")
            exit()


    def detect_sensor(self) -> None:
        """Method to detect whether user passed challenge or whole sensor"""
        try:
            self.passed_str = self.passed_str.split("-94,-124,")[1].split("-1,2,-94,-126")[0]
            self.whole_akam = True
        except IndexError:
            self.whole_akam = False


    def destruct_str(self) -> None:
        """Destructs challenge into smaller pieces"""
        self.deconstructed = self.passed_str.split(";")
        if len(self.deconstructed) == 5 or len(self.deconstructed) == 4:
            self.deconstructed = self.passed_str.split(";")[:4]
            self.deconstructed_mnlg = self.deconstructed[-1].split(",")
            self.deconstructed_mnlg = self.deconstructed_mnlg[:8] + \
                [",".join(self.deconstructed_mnlg[8:-3])] + self.deconstructed_mnlg[-3:]
        else:
            raise NonSensorException

    def print_deconstructed(self) -> None:
        """Pretty prints deconstructed challenge"""

        for item in zip(self.headers, self.deconstructed):
            print(Fore.CYAN + item[0] + Fore.RESET + ": " + item[1])

        print(Fore.GREEN + "mn_lg ingredients" + Fore.RESET)
        for mnlg_item in zip(self.mnlg_headers, self.deconstructed_mnlg):
            if mnlg_item[1][1]:
                color = Fore.GREEN
            else:
                color = Fore.RED

            print(Fore.CYAN + mnlg_item[0] + ": " + color + mnlg_item[1][0] + Fore.RESET)


    def check_mnlg(self) -> None:
        """Checks if values inside mn_lg are correct"""
        to_zip = [True] * 12
        if self.deconstructed_mnlg[3] != "".join(self.deconstructed_mnlg[:3]):
            to_zip[3] = False
        if self.deconstructed_mnlg[4] != self.deconstructed_mnlg[5]:
            to_zip[4], to_zip[5] = False, False
        if self.deconstructed_mnlg[7] != self.deconstructed_mnlg[3] + self.deconstructed_mnlg[5] \
            + self.deconstructed_mnlg[6]:
            to_zip[7] = False
        if int(self.deconstructed_mnlg[-1]) < int(self.deconstructed_mnlg[1]) \
            or len(self.deconstructed_mnlg[-1]) != 13:
            to_zip[11] = False

        self.deconstructed_mnlg = zip(self.deconstructed_mnlg, to_zip)

class NonSensorException(Exception):
    """Exception throwed when passed string is not valid"""
