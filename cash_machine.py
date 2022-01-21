import locale
from random import randint


class txt_fmt:
    blue = '\033[94m'
    green = '\033[92m'
    orange = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'


def cash_machine():
    global conf
    conf = {
        "debug": False,
        "name": "Kuma ATM",
        "banked_funds": 1000.00,
        "pin_attempts": 0,
        "pin_attempts_max": 3,
        "overdrawn_attempts": 0,
        "overdrawn_attempts_max": 0
    }

    def number_format(num, places=0):
        return locale.format_string("%.*f", (places, num), True)

    def generate_pin():
        num_string = ""
        while len(num_string) < 4:
            num_string += str(randint(0, 9))
        return num_string

    def is_pin_correct(pin):
        global conf
        # Be somewhat fair (lul); give 'em at least some chance to get it right
        cnt = 0
        while cnt < 100:
            cnt += 1
            pin_gen = generate_pin()
            pin_match = pin_gen == pin
            if conf["debug"]:
                is_match = {
                    "format": txt_fmt.green if pin_match else txt_fmt.red,
                    "display": "Match" if pin_match else "No Match",
                }
                print(f"{txt_fmt.blue}DEBUG: Iteration {cnt} · Generated Pin: {pin_gen}{txt_fmt.reset} · {is_match['format']}{is_match['display']}{txt_fmt.reset}")
            if pin_match:
                if conf["debug"]:
                    print(f"{txt_fmt.blue}DEBUG: Match found after {cnt} iterations. Stopped.{txt_fmt.reset}")
                return True
        return False

    def withdraw_funds(amount: float):
        global conf
        if conf["debug"]:
            print(f"{txt_fmt.blue}DEBUG: Overdrawn Attempts: {conf['overdrawn_attempts']} · Max Attempts: {conf['overdrawn_attempts_max']}{txt_fmt.reset}")
        if conf["overdrawn_attempts"] < conf["overdrawn_attempts_max"]:
            if (conf["banked_funds"]-amount) >= 0:
                conf["banked_funds"] -= amount
                print(f"{txt_fmt.green}Dispensing £{amount}{txt_fmt.reset} · {txt_fmt.green}{txt_fmt.bold}£{conf['banked_funds']}{txt_fmt.reset} {txt_fmt.green}remaining.{txt_fmt.reset}\n")
            else:
                conf["overdrawn_attempts"] += 1
                print(f"{txt_fmt.red}You don't have enough in your account.{txt_fmt.reset}\nBanked: {txt_fmt.bold}£{conf['banked_funds']}{txt_fmt.reset}")
        else:
            print(f"{txt_fmt.red}{txt_fmt.bold}MAXIMUM OVERDRAWN ATTEMPTS REACHED{txt_fmt.reset}\n{txt_fmt.red}Please contact your card issuer for assistance.{txt_fmt.reset}")
            quit()

    def show_bank_account():
        global conf
        print(f"{txt_fmt.blue}Welcome to {conf['name']}!\nYou have £{number_format(conf['banked_funds'])} available\n{txt_fmt.reset}")
        amount = input(f"{txt_fmt.blue}How much would you like to withdraw?{txt_fmt.reset}\n")
        withdraw_funds(amount)

    def login_to_atm(pin):
        global conf
        conf["pin_attempts"] += 1
        if conf["debug"]:
            print(f"{txt_fmt.blue}DEBUG: Pin Attempts: {conf['pin_attempts']} · Max Pin Attempts: {conf['pin_attempts_max']}{txt_fmt.reset}")
        pin_correct = is_pin_correct(pin)
        if conf["pin_attempts"] < conf["pin_attempts_max"]:
            if pin_correct:
                show_bank_account()
            else:
                print(f"{txt_fmt.red}{txt_fmt.bold}INVALID PIN{txt_fmt.reset}")
                welcome_screen(True)
        else:
            print(f"{txt_fmt.red}{txt_fmt.bold}MAXIMUM INCORRECT PIN ATTEMPTS REACHED.{txt_fmt.reset}\n{txt_fmt.red}Please contact your card issuer for assistance.{txt_fmt.reset}")

    def atm_art():
        atm = """
    ████████████████████████████████████
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██▒▒██████▒▒██████▒▒██████████▒▒▒▒██
    ██▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒██▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ████████████████████████████████████
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██▒▒████████████████████▒▒▒▒▒▒▒▒▒▒██
    ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
    ██▒▒██  ▒▒▒▒▒▒▒▒▒▒▒▒  ██████████████
    ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
    ██▒▒██  ▒▒▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒██
    ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██
    ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒██
    ██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██
    ██▒▒████████████████████▒▒▒▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ████████████████████████████████████
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ████████████████████████████████████
    """
        atm = atm.replace("█", f"{txt_fmt.green}█{txt_fmt.reset}")
        atm = atm.replace("▒", f"{txt_fmt.blue}▒{txt_fmt.reset}")
        return atm

    def welcome_screen(retry=False):
        global conf
        if retry == False:
            print(atm_art(), "\n")
            print(f"{txt_fmt.orange}{txt_fmt.bold}Welcome to {conf['name']}{txt_fmt.reset}\n")
        remaining_attempts = conf["pin_attempts_max"] - conf["pin_attempts"]
        s = "" if remaining_attempts == 1 else "s"
        pin = input(f"Please enter your PIN ({remaining_attempts} attempt{s} remaining): \n")
        login_to_atm(pin)

    welcome_screen()


cash_machine()
