from time import sleep
from random import randint, shuffle
from sys import stdout
name_list = ["charles", "charlie", "charles bucket", "charlie bucket"]
health = 100
lumpa_health = 25
boss_health = 200
chocolate_chips = 0
answer_k = ["K", "low"]
gold_berry = ["A:1", "B:2", "C:3", "D:4"]
wrong_berry = 7
hand = []
hand_value = 0
ace_in_hand = 0


class formatting:
    purple = '\033[95m'
    yellow = '\033[33m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    orange = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'

card_list = []
for i in range(0, 4):
    for j in range(1, 14):
        card_list.append(20*i + j)

def print_type(type, content):
    interval = .01 if type.lower() == "fast" else .03
    for char in content:
        sleep(interval)
        stdout.write(char)
        stdout.flush()


def colour(colour, string):
    return(f"\033[38;5;{colour}m{string}\033[0;0m")


def colour_back(colour, string):
    return(f"\033[48;5;{colour}m{string}\033[0;0m")


def intro():
    global name_list
    print_type("slow", "\n\nYou wake up in a royal bedroom, candy canes and lollipops line the walls. \nOk. It's time to get out of here. What is your name?")
    name = input("\n>> ")
    if name.lower() == "the best kind of prize is a surprise":
        print_type("slow", "\nThe ground beneath your feet shifts and roars, you're thrown to the floor. The whole bedroom, with you in it, is pulled into the Crazy Elevator...")
        cont()
        super_wonka()
    while name.lower() not in name_list:
        print_type("fast", "\nNo, Charles, you've forgotten again. The sweets still seems to have some power over you."
                   "\nYou're Charles Bucket, you've been here for over 50 years and you need to get home. \nLets try again.")
        name = input("\nWhat is your name? ")
        if name.lower() == "the best kind of prize is a surprise":
            print_type("slow", "\nThe ground beneath your feet shifts and roars, you're thrown to the floor. The whole bedroom, with you in it, is pulled into the Crazy Elevator...")
            cont()
            super_wonka()
    print_type("fast", "Ah Good, you remember.")
    hallway()


def hallway():
    print_type("fast", "\nLeaving your room into the hallway, trying not to make too much noise as your footsteps peel off the sticky floor, you notice a sign in the flickering light.\nLiquorice Lane is down the corridor to your left, Treacle Town is down the corridor to the right. There is also another corridor just ahead.\nYour memory is again drawing a blank on what any of this means but you need to choose quickly and keep moving. Where would you like to go?\n(L, R or ahead)")
    answer = input("I think I will go... \n").lower()
    valid_answer = False
    while valid_answer == False:
        if answer in ["l", "left"]:
            print_type("fast", "You choose Liquorice Lane and head down the corridor")
            cont()
            liq_lane()
        elif answer in ["r", "right"]:
            print_type("fast", "You choose treacle town and head down the corridor")
            cont()
            treacle_town()
        elif answer in ["a", "ahead"]:
            print_type("fast", "You head into a dark corridor that seems to go on for quite some time\nNeon lights get brighter and music gets louder as you approach the door at the end\nYou open the door and go inside")
            cont()
            casino_entrance()
        else:
            print("Come on Charles, left or right, we need to hurry")
            hallway()


def treacle_town():
    print_type("fast", colour(220, "\nWow! You enter the room and have to tip-toe around the edge of what appears to be a sweet scented oil spill.\nYou notice the walls, floor and ceiling of the entire room are completely covered in treacle. How will you get to the other side?\nThere is a box to the side of the door where you can access a pair of anti-treacle boots but the box is locked."))
    print_type("fast", "\nTo open the box, you must answer the question.")
    answer_name = input("\nWhich author created this crazy world of Willy Wonka?").lower()
    wrong_answer = 0
    while wrong_answer < 4:
        if answer_name.lower() == "roald dahl":
            print_type("slow", "\nCorrect! Lace up your boots and wade across the sweet treacle floor to the other side.")
            cont()
            chocolate_river()
        else:
            if wrong_answer > 2:
                print_type("slow", "You've taken too long Charles. An oompa loompa sneaks up behind you and smothers you with cotton candy chorolorm.")
                cont()
                intro()
            wrong_answer += 1
            print_type("fast", f"Try Again, You Have {4-wrong_answer} Attempts Left ")
            answer_name = input("\nWhich author created this crazy world of Willy Wonka?")


def casino_entrance():
    global chocolate_chips
    print_type("fast", colour(123, "\nAs neon lights get brighter and you hear the sound of music as you approach the door at the end.\nYou open the door and walk into the loudness and light.\nA well dressed Oompa Loompa, complete with waistcoat and monocle stands menacingly against the next door.\n'Ah, my next investment walks by.' He throws a pouch of chocolate chips by your side. 'Go make me rich, Charles.'"))
    print(colour(160, "        You gain 50 chocolate chips"))
    chocolate_chips = 50
    cont()
    casino()


def casino():
    print_type("fast", colour(123, "\nMoving forward, you enter what seems to be some kind of underground Casino. \nYou head past the depressed jingles of the slots machines and one particularly devastated Oompa Loompa\nwho you predict must have blown his whole, and presumably meagre, family savings on roulette."))
    global chocolate_chips
    print_type("fast", "\nThere's an open seat at both Rolo's Roulette and the Flapjack tables\nA : Head to the Flapjack Tables\nB : Try your luck on Rolo's Roulette\nC : Leave through the side door, you've no time for gambling")
    choice = input("\nAnswer = ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            print_type("fast", "\nYou head over to the Flackjack Tables" + colour(123, "\nThe dealer greets you.'Rules are simple, you draw for 21 then I do, I stick at 17 and always takes ace high. \nNo double downs, no splits. Odd are always evens. We draw, I win.'"))
            flapjack()
        elif choice == "b":
            valid_answer = True
            print_type("fast", "\nYou head over to the Roulette" + colour(123, "\n'I'm Rolo and this is my Roulette. My roulette, my rules, I'm Rolo, Got it? In my Roulette you put money on red, black or a number\nYou're right, you win. You're wrong, I'm Rolo... and I win. My rules, my Roulette, I'm Rolo. Ok? Let's play!'"))
            roulette()
        elif choice in ["c", "leave"]:
            valid_answer = True
            print_type("fast", "\nYou leave by the side door")
            cont()
            treacle_town()
        else:
            print("Concentrate Charles")
            choice = input("Answer = ").lower()

def do_roulette(bet):
    global chocolate_chips
    int_bet = int(bet)
    print_type("fast", f"The stake is {bet} and what's the bet?")
    choice = input("\nRed / Black / 0 to 36: ").lower()
    valid_answer2 = False
    while valid_answer2 == False:
        if choice.isnumeric() == True:
            if int(choice) >= 0 and int(choice) <= 36:
                valid_answer2 = True
                print_type("fast", f"You bet on {choice}. Let's spin...")
                result = randint(0, 36)
                print_type("fast", colour(123, f"\nAnd it's {result}."))
                if result == choice:
                    winnings = 35 * int_bet
                    print_type("fast", f" You won {formatting.green}{winnings}{formatting.reset} chocolate chips.")
                    chocolate_chips += winnings
                else:
                    print_type("fast", f" You lose {formatting.red}{int_bet}{formatting.reset} chocolate chips")
                    chocolate_chips -= int_bet
            else:
                print("That's not right")
                choice = input("\nRed / Black / 0 to 36: ").lower()
        elif choice.lower() in ["red", "black"]:
            valid_answer2 = True
            print_type("fast", f"You bet on {choice}. Let's spin...\n")
            result = randint(0, 36)
            if result == 0:
                print_type("fast", colour(255, colour_back(34, "       And it's green       ")))
                print_type("fast", f" You lose {formatting.red}{int_bet}{formatting.reset} chocolate chips")
                chocolate_chips -= int_bet
            elif result < 19:
                print_type("fast", colour(255, colour_back(16, "       And it's black       ")))
                if choice.lower() == "black":
                    print_type("fast", f" You win {formatting.green}{int_bet}{formatting.reset} chocolate chips")
                    chocolate_chips += int_bet
                else:
                    print_type("fast", f" You lose {formatting.red}{int_bet}{formatting.reset} chocolate chips")
                    chocolate_chips -= int_bet
            else:
                print_type("fast", colour(255, colour_back(160, "       And it's red       ")))
                if choice.lower() == "red":
                    print_type("fast", f" You win {formatting.green}{int_bet}{formatting.reset} chocolate chips")
                    chocolate_chips += int_bet
                else:
                    print_type("fast", f" You lose {formatting.red}{int_bet}{formatting.reset} chocolate chips")
                    chocolate_chips -= int_bet
        else:
            print("That's not right")
            choice = input("Red / Black / 0 to 36: ").lower()

def roulette():
    global chocolate_chips
    print_type("fast", f"\nYou've got {chocolate_chips} chocolate chips, how much you betting?        \033[3;31m number / 'leave' \033[0;0m   ")
    bet = input().lower()
    if bet == 'leave':
        casino()
    valid_answer = False
    while valid_answer == False:
        if bet.isnumeric() == True and int(bet) <= chocolate_chips and int(bet) > 0:
            valid_answer = True
            do_roulette(bet)
        else:
            print("That's not right Charles")
            bet = input(f"\nYou've got {chocolate_chips} chocolate chips, how much you betting?     \033[3;31m number / 'leave' \033[0;0m ").lower()
            if bet == 'leave':
                casino()
    if chocolate_chips < 1:
        print_type("fast", "\n'A Charles with no chips is no Charles worth having' The bouncers escort you out and down to liquorice lane.")
        cont()
        liq_lane()
    elif chocolate_chips > 149:
        print_type("fast", "\n'OK, Mr Highroller the boss said you can have access straight to dessert island.\nYou don't have to go, but you can't stay'")
        cont()
        dessert_island()
    roulette()


def card_read(num):
    card = ""
    suit = ""
    if num < 15:
        suit = "Hearts"
    elif num < 35:
        num -= 20
        suit = "Spades"
    elif num < 55:
        num -= 40
        suit = "Diamonds"
    else:
        num -= 60
        suit = "Clubs"
    if num == 1:
        card = "Ace"
    elif num < 11:
        card = num
    elif num == 11:
        card = "Jack"
    elif num == 12:
        card = "Queen"
    else:
        card = "King"
    return str(card) + " of " + suit


def card_value(num):
    if num >= 15:
        if num < 35:
            num -= 20
        elif num < 55:
            num -= 40
        else:
            num -= 60
    if num == 1:
        return 11
    elif 1 < num < 11:
        return num
    else:
        return 10


def flapjack():
    global chocolate_chips
    print_type("fast", f"\nYou've got {chocolate_chips} chocolate chips, how much you betting?        \033[3;31m number / 'leave' \033[0;0m   ")
    bet = input().lower()
    if bet == 'leave':
        casino()
    valid_answer = False
    while valid_answer == False:
        if bet.isnumeric() == True and int(bet) <= chocolate_chips and int(bet) > 0:
            valid_answer = True
            int_bet = int(bet)
            play_flapjack(int_bet)
        else:
            print("That's not right")
            bet = input(f"\nYou've got {chocolate_chips} chocolate chips, how much you betting?     \033[3;31m number / 'leave' \033[0;0m ").lower()
            if bet == 'leave':
                casino()

def play_flapjack(num):
    global hand_value, ace_in_hand, player_bust, chocolate_chips
    shuffle(card_list)
    player_bust = False
    ace_in_hand = 0
    if card_list[0] in [1, 21, 41, 61]:
        ace_in_hand += 1
    if card_list[1] in [1, 21, 41, 61]:
        ace_in_hand += 1
    hand_value = card_value(card_list[0]) + card_value(card_list[1])
    print_type("fast", f"You're dealt {formatting.cyan}{card_read(card_list[0])}{formatting.reset} and {formatting.cyan}{card_read(card_list[1])}{formatting.reset} for a score of {formatting.cyan}{hand_value}{formatting.reset}")
    if hand_value == 22:
        bust()
    j = 0
    player_stick = False
    while hand_value < 21 and player_stick == False:
        choice = input("\nStick or twist Charles?                           \033[3;31m 'stick' or 'A'/'twist' or 'B' \033[0;0m \n").lower()
        valid_answer = False
        while valid_answer == False:
            if choice.lower() in ["twist", "b"]:
                valid_answer = True
                if card_list[2+j] in [1, 21, 41, 61]:
                    ace_in_hand += 1
                hand_value += card_value(card_list[2+j])
                print_type("fast", f"\nYou twist, you're dealt {formatting.cyan}{card_read(card_list[2+j])}{formatting.reset} for a score of {formatting.cyan}{hand_value}{formatting.reset} ")
                bust()
                j += 1
            elif choice.lower() in ["stick", "a"]:
                valid_answer = True
                print_type("fast", f"You stick at {formatting.cyan}{hand_value}{formatting.reset}")
                player_stick = True
            else:
                print("That's not right Charles")
                choice = input("Stick or twist Charles?                           \033[3;31m 'stick' or 'A'/'twist' or 'B' \033[0;0m \n").lower()
    dealer_bust = False
    dealer_card1 = card_list[51]
    dealer_card2 = card_list[50]
    dealer_hand_value = card_value(dealer_card1) + card_value(dealer_card2)
    print_type("fast", f"\nDealer has {formatting.blue}{card_read(dealer_card1)}{formatting.reset} and {formatting.blue}{card_read(dealer_card2)}{formatting.reset} with a score of {formatting.blue}{dealer_hand_value}{formatting.reset}")
    i = 0
    while dealer_hand_value < 17:
        dealer_hand_value += card_value(card_list[49-i])
        print_type("fast", f"\nDealer draws {formatting.blue}{card_read(card_list[49-i])}{formatting.reset} for a score of {formatting.blue}{dealer_hand_value}{formatting.reset}")
        i += 1

    if dealer_hand_value > 21:
        print_type("fast", " Dealer goes bust!")
        dealer_bust = True

    if dealer_bust == True:
        chocolate_chips += num
        print_type("fast", f"\nYou win and have  {formatting.green}{chocolate_chips}{formatting.reset} chocolate chips")
    elif player_bust == True:
        chocolate_chips -= num
        print_type("fast", f"\nYou lose and have {formatting.red}{chocolate_chips}{formatting.reset} chocolate chips left")
    elif hand_value > dealer_hand_value:
        chocolate_chips += num
        print_type("fast", f"\nYou win and have {formatting.green}{chocolate_chips}{formatting.reset} chocolate chips")
    else:
        chocolate_chips -= num
        print_type("fast", f"\nYou lose and have {formatting.red}{chocolate_chips}{formatting.reset} chocolate chips left")

    if chocolate_chips < 1:
        print_type("fast", "\n'A Charles with no chips is no Charles worth having'. The bouncers escort you out and down to liquorice lane.")
        cont()
        liq_lane()
    elif chocolate_chips > 149:
        print_type("fast", "\n'OK, Mr Highroller the boss said you can have access straight to dessert island. You don't have to go but you can't stay'")
        cont()
        dessert_island()
    flapjack()


def bust():
    global hand_value, ace_in_hand, player_bust
    if hand_value > 21 and ace_in_hand > 0:
        hand_value -= 10
        print(f"Ace goes to low, score now {formatting.cyan}{hand_value}{formatting.reset}")
        ace_in_hand -= 1
    elif hand_value > 21:
        print("That's bust")
        player_bust = True


def liq_lane():
    print_type("fast", colour(255, colour_back(16, "\nYou enter through an archway out onto a ledge overlooking Liquorice Lane, a discreet side alley that links each side of the factory.\nYou notice there is an oompa loompa at the foot of the stairs in front of you, sweeping the liquorice cobbles. He's looking so dejected he may not even notice you.\nHowever, the only other way across is a red rope liquorice bridge that will take you over the lane and back into the factory.\nWhich way would you like to go?")))
    print("\nA : Climb down the ladder, past the oompa Loompa\nB : Hold onto the liquorice ropes and head over the bridge")
    choice = input("Answer= ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            print_type("fast", "You decide to climb down the stairs and onto Liquorice Lane")
            result = randint(0, 2)
            if result in [0, 1]:
                print_type("fast", "\nThe oompa loompa looks at you as you pass, complains about his job, how underpaid he is, and carries on sweeping."
                           "\nYou go through a door, out of the lane and back into the factory")
                cont()
                jelly_bean_bath()
            else:
                print_type("fast", "\nThe oompa loompa, on seeing you, lets out a shriek and dozens of oompa loompa surround you in seconds. \nForcing narcotic sweets down your throat, they carry you back to your room.\n'Not today, Charles. Take your pills and let's get back to your room for a sleep'")
                cont()
                intro()
        elif choice == "b":
            valid_answer = True
            print_type("fast", "\nYou decide to cross the bridge, quietly without being noticed and head towards a large wooden door on the other side.")
            result = randint(0, 2)
            if result in [0, 1]:
                print_type("fast", "\nLuckily you go undetected across the bridge.\nYou enter the door, back into the factory")
                cont()
                jelly_bean_bath()
            else:
                print_type("fast", "\nYou begin to cross the red rope bridge but as you approach the halfway point, oompa loomp begin to assemble on Liquorice Lane below you\nSuddenly they start to appear on either side of the bridge too, shaking the bridge until you lose your grip and fall onto the crowd below.\nThe oompa loompa carry you back to your room to sleep.")
                cont()
                intro()
        else:
            print("Sorry, that isn't an option now Charles. It's between the ladder and the bridge. Make a decision, quickly.")
            choice = input("Answer= ").lower()


def jelly_bean_bath():
    answer_eat = ["eat", "munch", "swallow", "scram", "inhale the beans", "chew"]
    print_type("fast", colour(37, "\nWhile continuing along the path you have chosen, the teal floor suddenly opens up and turns into jelly beans leading you to fall down into a chute.\nYou slide to the bottom of the chute and land in a pool of jelly beans.You must eat your way out to survive!"))
    print("\nEat?" "       \033[3;33mType 'eat' to eat\033[0;0m")
    choice = input(">> ").lower()
    jelly_beans = 0
    weight = 0
    while jelly_beans < 6 and weight < 5:
        valid_answer = False
        while valid_answer == False:
            if choice in answer_eat:
                valid_answer = True
                jelly_beans += 1
                if jelly_beans >= 5:
                    print_type("slow", "\nChewing, chewing all day long, Chewing, chewing all day long.\nYou go on chewing till at last, your chewing muscles grow so fast\n" + f"{formatting.purple}A rainbow{formatting.blue} of light{formatting.cyan} shines through{formatting.green} the multicoloured{formatting.yellow} jelly beans.{formatting.red} You've dug your way out.{formatting.reset}\n")
                    cont()
                    chocolate_statue()
                print_type("fast", "You munch on mouthfuls of jelly beans but there's still more to come.\n")
            else:
                weight += 1
                if weight >= 4:
                    valid_answer = True
                    print("The weight of the jelly beans crushes your frail bones\n")
                    cont()
                    game_over()
                else:
                    print_type("fast", "You feel the weight of the jelly beans slowly crush you as you do nothing")
                    choice = input("\n>>").lower()
        choice = input(">> ").lower()


def chocolate_statue():
    print_type("fast", colour(192, "\nYou enter a tall, lime green room with piles of old, caramel coated equipment scattered across the floor.\nTo the side of the room, you see a towering figure made of what seems to be pure chocolate guarding the door."))
    print("\nA : Casually stroll to the exit\nB : Pick up a sugar coated hammer and hurl it at the chocolate figure\nC : Slowly creep through the room, being sure to evade the metal instruments")
    choice = input(">> ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            result = randint(0, 2)
            if result < 2:
                print_type("slow", "\nYou casually stroll through the room with nothing to worry about and on to the next one")
                cont()
                violets_room()
            else:
                print_type("slow", "\nYour casual stroll is interrupted! Amidst the sugar coated floors, you step on a rake. \nThe handle of which launches straight at your head, knocking you out cold. You should have been more careful, Charles.")
                cont()
                intro()
        elif choice == "b":
            valid_answer = True
            print_type("fast", "\nThats statues suspicious. You hurl the hammer right at the middle of the figure. \nIt's chocolate armor cracks, revealing not a pure chocolate core but three oompa loompas stacked on top of one another."
                       "\nThe middle one is brutally injured by your vicious attack. The other two run at you but leaping through the gap in their formation, you move on to the next room.")
            cont()
            violets_room()
        elif choice == "c":
            valid_answer = True
            print_type("fast", "\nYou slowly approach the door but in the time it has taken, the towering figure's chocolate armour breaks \napart revealing not a pure chocolate core but three Oompa Loompas stacked on top of one another"
                       "\nThey charge at you, their three pronged attack cuts of any hope of exit. They got you.")
            cont()
            intro()
        else:
            print("That does nothing Charles")
            choice = input(">>").lower()


def violets_room():
    print_type("fast", colour(201, "\nYou enter a room filled with the sweet smell of blueberries. Lilac walls alight with periwinkle candles and a plush mauve carpet underneath your feet. \nIt's Violet Beauregaurde...") + colour(93, "'OH Charles, it's you. Trying to escape again? Well don't bother. You'll always be trapped in here and I'll always be a blueberry. Accept it.") + colour(200, "\nThis is the fanciest room in the factory Charlie. Just take a rest. I know you want to.'"))
    print(colour(165, "\nA : Resist the urge to rest\nB : This is a nice room, a quick rest should give you more energy"))
    choice = input("Answer= ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            print_type("fast", colour(129, "\nThe urge to sleep is strong but you attempt to resist it"))
            result = randint(0, 2)
            if result in [0, 2]:
                print_type("slow", colour(129, "\nViolets 'persuasive' words can't sway you, you bolt through the purple haze and out of the room"))
                cont()
                blueberry_room()
            else:
                print_type("fast", colour(129, "\nYour attempts are futile and you fall into slumber"))
                cont()
                intro()
        elif choice == "b":
            valid_answer = True
            print_type("fast", colour(129, "\nYou close for your eye for just a second, but that second leads to hours...you disappear into sweet slumber."))
            cont()
            intro()
        else:
            print("Not an option Charles")
            choice = input("Answer= ").lower()


def dessert_island():
    print_type("slow", colour(226, "\n                         You are now on the dessert island!\n                     Can you finally escape and get back home?. "))
    print_type("slow", colour(27, "\nFeeling hungry as you haven't eaten for 50 years. You see a table with 3 different desserts."))
    print("\nA: Peach Brown Betty Slice!\nB: Summer Berry Grunt Cake!\nC: Tiny Raspberry Fool!")
    choice = input("I think I will eat ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            print_type("slow", "WOW!\nThe peach brown betty slice turned you into a betty")
            print_type("fast", "\nYou are now stuck unless you answer this question right")
            betty_slice()
        elif choice == "b":
            valid_answer = True
            print_type("slow", "\nGreat!!! The summer berry grunt cake teleported you to the next room")
            cont()
            blueberry_room()
        elif choice == "c":
            valid_answer = True
            print_type("slow", "\nYou picked the Tiny raspberry fool and shrink into a raspberry\nThe effect may ware off.... Maybe")
            cont()
            game_over()
        else:
            print("That's not right Charles")
            choice = input("I think I will eat ").lower()


def betty_slice():
    print_type("slow", "\nHow did this happen?")
    print("\nA: Your eyes are bigger than your belly \nB: I've not eaten in 50 years what did you expect")
    choice = input("My answer is ").lower()
    valid_answer = False
    result = randint(0, 10)
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            if result <= 6:
                print_type("slow", "\nYou manage to shake off the effect ")
                cont()
                blueberry_room()
            else:
                print_type("slow", "\nThe cake is a lie")
                game_over()
        elif choice == "b":
            valid_answer = True
            if result >= 7:
                print_type("slow", "\nYou manage to shake off the effect ")
                cont()
                blueberry_room()
            else:
                print_type("slow", "\nThe cake is a lie ")
                game_over()
        else:
            print("That's not right Charles")
            choice = input(">>").lower()


def blueberry_room():
    global wrong_berry, gold_berry
    print_type("fast", colour(21, colour_back(255, "\nYou enter a bright white room. You see writing on the wall in what appears to be blueberry juice.\nThe writing states: \nFour golden blueberries sit on platforms in a line that controls the lock. \nEat them in order and more wonders await beyond. If you eat them in the wrong order.. well, you will see")))
    wrong_berry = 7
    blueberry_room_new()

def blueberry_room_new(iteration:int = 0):
    global wrong_berry, gold_berry
    gold_berry = ["A", "B", "C", "D"]
    sequence = "CADB"
    print_type("fast", f"\nYou look around the room and see the platforms. Each marked with a number\n{gold_berry}")
    choice = input(" Guess I'll start with\n ").lower()
    valid_answer = False
    while valid_answer == False and wrong_berry > 0:
        letter = sequence[iteration]
        if choice == letter.lower():
            valid_answer = True
            print("The door flings open with force like its upset you guessed right")
            gold_berry.remove(letter.upper())
            iteration += 1
            blueberry_room_new(iteration) if iteration < 3 else blueberry_room4()
        elif wrong_berry == 1:
            print_type("fast", "An oompa Loompa looks at you, clearly sick of this and he drags you away")
            game_over()
        elif choice != letter.lower():
            valid_answer = True
            wrong_berry -= 1
            print_type("slow", f"An oompa Loompa pops up out of nowhere holding a sign {wrong_berry} tries remain")
            blueberry_room_new(iteration)
        else:
            print_type("slow", "Its not hard to pick a berry up")
            choice = input("Guess I'll start with ").lower()


def blueberry_room2():
    global wrong_berry, gold_berry
    print_type("slow", f"One down, three to go\n{gold_berry}")
    choice = input(" Next will be\n ")
    valid_answer = False
    while valid_answer == False:
        if choice == "c":
            print("You ate that one before. Stop wasting time")
            blueberry_room2()
        elif choice == "a":
            valid_answer = True
            print("The door flings open with force like its upset you guessed right")
            gold_berry.remove("A:1")
            blueberry_room3()
        elif wrong_berry == 1:
            print_type("fast", "An oompa loompa looks at you, clearly sick of this and he drags you away")
            game_over()
        elif choice in ["b", "d"]:
            valid_answer = True
            wrong_berry -= 1
            print(f"An alarm sounds and oompa ooompa drag you back into the first room {wrong_berry} tries remain")
            blueberry_room_new()
        else:
            print("Come on. It's a berry! Eat one!")
            blueberry_room2()


def blueberry_room3():
    global wrong_berry, gold_berry
    print_type("slow", f"Two down, Two to go\n{gold_berry}")
    choice = input(" Next will be\n ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "b":
            if wrong_berry == 1:
                print("An oompa Loompa looks at you, clearly sick of this and he drags you away")
                game_over()
            wrong_berry -= 1
            print(f"An alarm sounds and oompa Loompa drags you back into the first room {wrong_berry} tries remain")
            blueberry_room_new()
        if choice in ["a", "c"]:
            valid_answer = True
            print("You ate that one before. Stop wasting time")
            blueberry_room3()
        elif choice == "d":
            valid_answer = True
            print("The door flings open with force")
            gold_berry.remove("D:4")
            blueberry_room4()
        else:
            print("Come on its a berry eat one")
            blueberry_room3()


def blueberry_room4():  # End of blueberry chain
    global gold_berry
    print(f" Three down, one remaining\n{gold_berry}")
    choice = input("Finally I'll grab the last berry on platform\n").lower()
    valid_answer = False
    while valid_answer == False:
        if choice in ["a", "c", "d"]:
            valid_answer = True
            print("Really stop messing around! You only have one berry to pick.")
            blueberry_room4()
        elif choice == "b":
            valid_answer = True
            print_type("slow", "The final door swings open letting you finally leave this nightmare of a room")
            print_type("slow", "\nYou can now get out of the blueberry room and finally get closer to home!")
            cont()
            crazy_elevator()
        else:
            choice = input("Finally I'll grab the last berry on platform\n").lower()


def walk_to_boss():
    global health, lumpa_health, boss_health
    print_type("fast", colour(212, "\nYour legs are starting to feel heavy again as the size of the factory journey takes its toll.\nWhile walking through a darkened part of the room, you feel yourself being picked up by something and realise its those pesky oompa loompas again!\nThey arm and leg you, swinging you from left to right, loudly singing as they do. \nThey lie you down and strap you in to what you realise is a chocolate chute at the end of the room.You fly down the chute at ridiculous speeds. \nYou manage to escape the chute's straps and fall into a nearby room where an oompa loompa guard immediately begins to attack you."))
    print("\nWhat will you do?")
    health = 100
    lumpa_health = 25
    boss_health = 200
    lumpa_jab = 5
    lumpa_punch = 60
    while health >= 30 and lumpa_health > 0:
        roll = randint(0, 6)
        block = randint(15, 40)
        punch = randint(15, 30)
        choice = input("\n\nA:Block / B:Punch     >> ").lower()
        if choice in ["a", "block"] and roll != 6:
            health -= block
            print_type("fast", f"\nYou block the attack but still it still hurts {health} health left")
        elif choice in ["a", "block"] and roll == 6:
            health -= lumpa_punch
            print_type("fast", f"\nYou try to block but fail to do so in time the punch hits you,{health} health left")
        elif choice in ["b", "punch"] and roll != 6:
            lumpa_health -= punch
            print_type("fast", f"\nYou swing with all your might landing a hard blow on the guard {lumpa_health} health remaining")
        elif choice in ["b", "punch"] and roll == 6:
            health -= lumpa_jab
            print_type("fast", f"\nYou swing with all your might and miss by miles\nGot both contacts in one eye?\n {health} health remaining")
        else:
            print("No time for messing")
    if health <= 30:
        print_type("fast", "\nYou fall down due to being wore out and get dragged back into your room")
        cont()
        intro()
    elif lumpa_health <= 0:
        print_type("fast", "\nYou eventually manage to get the better of the guard and make your way towards a pair of huge double doors.")
        cont()
        end_room()


def display_stats(boss_health, health):
    spacer = " " * 30
    return f"{spacer}{formatting.orange}Wonka Health: {boss_health}{spacer}Charles Health: {health}{formatting.reset}"


def end_room():
    punch_dmg = 15
    kick_dmg = 30
    low_blow = 9001
    boss_dmg = 30
    energy_drink = 75
    global health, boss_health
    print_type("slow", colour(165, "As you approach the big double doors, they slowly open automatically with sweet smoke bellowing from the room\n Standing in the middle of the room, blocking the main exit is Willy Wonka himself\nAh, young Charlie Bucket. Or should I call you Old Charles now?. You know you can't escape old man. Time to put you back to sleep.\nThe fight for freedom begins as Wonka rushes you immediately."))
    health += energy_drink
    while health >= 11 and boss_health >= 1:
        choice = input("\n\nA:Block / B:Punch / C:Kick    >> ").lower()
        crit_dmg = randint(2, 4)
        luckroll = randint(0, 6)
        block_dmg = randint(20, 60)
        wonka_attack()
        if choice in ["a", "block"] and luckroll < 4:
            health -= block_dmg
            print_type("fast", f"\nYou block the attack but still it still hurts, you take {block_dmg}{display_stats(boss_health, health)}")
        elif choice in ["a", "block"] and luckroll >= 4:
            health -= boss_dmg
            print_type("fast", f"\nYou try to block but fail to do so in time the punch hits, you take {boss_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["b", "punch"] and luckroll >= 4:
            boss_health -= punch_dmg * crit_dmg
            print_type("fast", f"\nYou swing wild and seem to hit a weak spot for {punch_dmg * crit_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["b", "punch"] and luckroll <= 4:
            boss_health -= punch_dmg
            print_type("fast", f"\nPillow fists, your blow ricochets off his sugar harderened coat for {punch_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["c", "kick"] and luckroll >= 5:
            boss_health -= kick_dmg*crit_dmg
            print_type("fast", f"\nFootballs coming home, your high jump kick connects for {kick_dmg*crit_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["c", "kick"] and luckroll < 5:
            boss_health -= kick_dmg
            print_type("fast", f"\nYou hit him with a sharp leg kick for {kick_dmg} damage{display_stats(boss_health, health)}")
        elif choice in answer_k:
            boss_health -= low_blow
            print_type("slow", "\nIt's over 9000")
        else:
            print("\nDon't just stand there, do something!")
    if health <= 10:
        print_type("fast", "\nYou're knocked off your feet and don't have the strength get up. You get dragged back into your room")
        game_over()
    elif boss_health <= 0:
        print_type("slow", "\n\nHe is now on his last legs, you give him one final blow and you have finally defeated Willy Wonka")
        print_type("slow", "\nYou head for the exit and live hapilly ever after.\n")
        cont()
        outro()


def outro():
    print_type("slow", "\nThank you for playing Charles and the Chocolate Factory!!!")
    print_type("fast", "\nThe best kind of prize is a surprise")
    choice = input("\nPlay again?").lower()
    intro() if choice in ["yes", "y", "a"] else quit()


def chocolate_river():
    print_type("fast", colour(130, "\nYou hear the sound of a splash! Something sparkles in the corner of your eye and you head over to check it out.It's a chocolate river!! Mmmm Charles likes chocolate!\nYou see a Giant Donut Dinghy that you can sit in to float down the chocolate river .You jump in the Donut Dinghy, sliding through the chocolate river at some speeds! You hit a fork with 2 separate path directions.\nThere's no earthly way of knowing which direction we are going. There's no knowing where we're rowing or which way the river's flowing.\nWhich path do you take?\n(L or R)"))
    answer = input("\nMy choice is ").lower()
    if answer in ["l", "left"]:
        print_type("slow", "You head towards Dessert Island")
        cont()
        dessert_island()
    elif answer in ["r", "right"]:
        print_type("slow", "You head towards Toffee Tavern")
        cont()
        toffee_tavern()
    else:
        print("You need to enter left or right")
        chocolate_river()


def toffee_tavern():
    print_type("fast", colour(136, "You creep into what seems like an old toffee tavern.You're beginning to breathe a little heavily now and your elderly legs are really tiring.\nLuckily you spot a sign indicating that the toffee tavern's taps have Jolly Juice from Wonka energy.This is your chance to go running down the halls like the old days\nYou wait for the coast to be clear and approach the taps but they aren't labelled."))
    answer = input("\nChoose left tap (L) or right tap (R): ").lower()
    valid_answer = False
    while valid_answer == False:
        if answer in ["l", "left"]:
            valid_answer = True
            print_type("slow", "\nCandy is dandy, but liquor is quicker. You drink the Jolly Juice and swagger on forward.")
            cont()
            matrix()
        elif answer in ["r", "right"]:
            print_type("slow", "\nOh dear. Whatever drink this is has given you root beer goggles as you head back to your room with a couple of oompa loompas. ")
            cont()
            intro()
        else:
            answer = input("\nChoose left tap (L) or right tap (R): ").lower()
            print("Enter L or R")


def matrix():
    print_type("fast", colour(118, "\nYou pass through a dimly lit hallway. Ahead of you stands a mysterious oompa loompa, seemingly acting on his own.\nHe wears a black trench coat and nose pinching glasses that hide his eyes. He reaches out both hands, each grasping a chocolate bonbon."))
    print_type("slow", "\nYou know the drill Charles. Red or Blue?\nA : Red\nB : Blue")
    choice = input("\n>> ").lower()
    valid_answer = False
    while valid_answer == False:
        if choice in ["red", "a"]:
            valid_answer = True
            print_type("slow", "\nYou take the red bonbon - you stay in wonderland, let's see how deep the rabbit hole goes.")
            cont()
            blueberry_room()
        elif choice in ["blue", "b"]:
            valid_answer = True
            print_type("slow", "\nYou take the blue bonbon - the story ends, you wake up in your bed and believe whatever you want to believe.")
            cont()
            intro()
        else:
            print("Try again Charles")
            choice = input(">>")


def crazy_elevator():
    print_type("fast", colour(147, "\nYou have a quick rest to get your breath back when Willy Wonka suddenly appears out of nowhere.'Having fun?' he says in an awkward sounding voice\nHe then disappears in a poof of smoke....\nSuddenly you hear an elevator noise 'Ding!'. Elevator doors suddenly open to your left. You enter the elevator and  it immediately begins to fire off at super speed in all directions. "))
    print("\nWhich path do you choose? Up Down left or right?")
    answer = input("\nChoose left (L), right (R), Up (U) and Down (D): ").lower()
    valid_answer = False
    while valid_answer == False:
        if answer in ["l", "left"]:
            valid_answer = True
            print_type("slow", "\nThe Crazy Elevator has taken you to Dessert Island")
            cont()
            dessert_island()
        elif answer in ["r", "right"]:
            valid_answer = True
            print_type("slow", "\nThe Crazy Elevator has taken you to Violets Room.")
            cont()
            violets_room()
        elif answer in ["up", "u"]:
            valid_answer = True
            print_type("slow", "\nThe Crazy Elevator has taken you to a room where you will meet Willy Wonka.")
            cont()
            walk_to_boss()
        elif answer in ["d", "down"]:
            valid_answer = True
            print_type("slow", "\nThe Crazy Elevator has taken you to a hallway.")
            cont()
            matrix()
        else:
            print("Come on Charles. Enter L, R, U, D ")
            answer = input(">>").lower()


def wonka_attack():
    global health, boss_health
    attack = randint(0, 9)
    if attack in [0, 1, 2, 3]:
        health -= 10
        print_type("fast", f"Willy slaps you on the head with his cane for 10 damage{display_stats(boss_health, health)}")
    elif attack in [4, 5, 6]:
        health -= 30
        print_type("fast", f"Mr Wonka hurls jawbreakers at you from range for 30 damage{display_stats(boss_health, health)}")
    elif attack in [7, 8]:
        health -= 60
        print_type("fast", f"He hits you with the flying elbow for 60 damage{display_stats(boss_health, health)}")
    else:
        health -= 150
        print_type("fast", f"Willy Wonka uses hyper beam for 150 DAMAGE{display_stats(boss_health, health)}\n{formatting.red}WONKA WONKA{formatting.reset}")


def game_over():
    print_type("slow", "\nYou Lose. Good Day, Sir.\n\nGiving up so easy?\nDon't you want to escape")
    print("\nA: Try again....")
    choice = input("Please enter A or B to quit\n").lower()
    valid_answer = False
    while valid_answer == False:
        if choice == "a":
            valid_answer = True
            print("Thats the ticket")
            intro()
        elif choice == "b":
            valid_answer = True
            print("shame")
            quit()
        else:
            print("Invaild")
            choice = input("Enter 'A' to go again / 'B' to quit").lower()


def cont():
    input(colour(245, "\n  --press enter to continue--  "))


def super_wonka():
    global health, boss_health
    health = 225
    boss_health = 500
    punch_dmg = 15
    kick_dmg = 30
    low_blow = 9
    boss_dmg = 30
    engery_drink = 100
    print_type("slow", colour(165, "\nYou leave the elevator out into the factory's former car park. You come to realise that this is likely the first time you've been outside in 50 years. \nThe factory gates lie ahead, lit only by the stars that glaze the night sky.\nBut suddenly, an enormous presence casts a shadow over everything, as Willy Wonka, like he's never been seen before, approaches the space between you and the gates.\nThe sheer size of the shadow makes it clear that this is no ordinary Wonka. He is enormous. He can sense your fear as the size of the task to beat him becomes apparent. \n'The suspense is terrible. I hope it'll lasts' he says as you begin to tremble. \nbYou'll likely never get this close to the exit again. You must attack him now, no matter how big he is."))
    print_type("slow", "\nWilly Wonka starts to rush you!!!")
    while health >= 11 and boss_health >= 1:
        choice = input("\n\nA:Block / B:Punch / C:Kick / D:Heal   >> ").lower()
        crit_dmg = randint(2, 4)
        luckroll = randint(0, 6)
        block_dmg = randint(20, 60)
        if choice in ["a", "block"] and luckroll < 4:
            health -= block_dmg
            print_type("fast", f"\nYou block the attack but still it still hurts, you take {block_dmg}{display_stats(boss_health, health)}")
        elif choice in ["a", "block"] and luckroll >= 4:
            health -= boss_dmg
            super_wonka_attack()
            print_type("fast", f"\nYou try to block but fail to do so in time the punch hits, you take {boss_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["b", "punch"] and luckroll >= 5:
            boss_health -= punch_dmg * crit_dmg
            print_type("fast", f"\nYou swing wild and seem to hit a weak spot for {punch_dmg * crit_dmg} damage, he stumbles{display_stats(boss_health, health)}")
        elif choice in ["b", "punch"] and luckroll <= 4:
            boss_health -= punch_dmg
            print_type("fast", f"\nPillow fists, your blow ricochets off his sugar harderened coat for {punch_dmg} damage{display_stats(boss_health, health)}")
            super_wonka_attack()
        elif choice in ["c", "kick"] and luckroll >= 5:
            boss_health -= kick_dmg*crit_dmg
            print_type("fast", f"\nFootballs coming home, your high jump kick connects for {kick_dmg*crit_dmg} damage{display_stats(boss_health, health)}")
            super_wonka_attack()
        elif choice in ["c", "kick"] and luckroll < 5:
            boss_health -= kick_dmg
            super_wonka_attack()
            print_type("fast", f"\nYou hit him with a sharp leg kick for {kick_dmg} damage{display_stats(boss_health, health)}")
        elif choice in ["d", "heal"]:
            health += engery_drink
            print_type("fast", f"\nYou crack open a cold one {engery_drink} health recovered{display_stats(boss_health, health)}")
            super_wonka_attack()
        elif choice in answer_k:
            boss_health -= low_blow
            print_type("slow", "\nIt's over 9000")
            super_wonka_attack()
        else:
            print("\nDon't just stand there, do something!")
            super_wonka_attack()
    if health <= 10:
        print_type("fast", "\nYou're knocked off your feet and don't have the strength get up. You get dragged back into your room")
        cont()
        game_over()
    elif boss_health <= 0:
        print_type("fast", "\n\nWilly Wonka is now on his last legs you give him 1 last final blow and you have finally defeated Willy Wonka\nYou head for the exit and live hapilly ever after.\n")
        cont()
        outro()


def super_wonka_attack():
    global health, boss_health
    attack = randint(0, 13)
    if attack in [0, 1, 2, 3]:
        health -= 30
        print_type("fast", f"\nWilly whips at you with red vine liquorice for 30 damage{display_stats(boss_health, health)}")
    elif attack in [4, 5, 6]:
        health -= 40
        print_type("fast", f"\nMr Wonka bombards you with his bonbon bazooka for 40 damage{display_stats(boss_health, health)}")
    elif attack in [7, 8]:
        health -= 60
        print_type("fast", f"\nHe showers you in molten sugar for 60 damage{display_stats(boss_health, health)}")
    elif attack in [9, 10, 11]:
        boss_health += 50
        print_type("fast", f"\nWonka takes a breaks and heals for 50 health{display_stats(boss_health, health)}")
    else:
        health -= 200
        print_type("fast", f"\nWilly Wonka uses hyper beam for 200 DAMAGE{display_stats(boss_health, health)}\n {formatting.red}WONKA WONKA{formatting.reset}")


def title_screen():
    print(colour(165, r"""
      _________ .__                 .__                                        .___      __  .__
      \_   ___ \|  |__ _____ _______|  |   ____   ______    _____    ____    __| _/    _/  |_|  |__   ____
      /    \  \/|  |  \\__  \\_  __ \  | _/ __ \ /  ___/    \__  \  /    \  / __ |     \   __\  |  \_/ __ \
      \     \___|   Y  \/ __ \|  | \/  |_\  ___/ \___ \      / __ \|   |  \/ /_/ |      |  | |   Y  \  ___/
       \______  /___|  (____  /__|  |____/\___  >____  >    (____  /___|  /\____ |      |__| |___|  /\___  >
              \/     \/     \/                \/     \/          \/     \/      \/                \/     \/
_________ .__                        .__          __             ___________              __
\_   ___ \|  |__   ____   ____  ____ |  | _____ _/  |_  ____     \_   _____/____    _____/  |_  ___________ ___.__.
/    \  \/|  |  \ /  _ \_/ ___\/  _ \|  | \__  \\   __\/ __ \     |    __) \__  \ _/ ___\   __\/  _ \_  __ <   |  |
\     \___|   Y  (  <_> )  \__(  <_> )  |__/ __ \|  | \  ___/     |     \   / __ \\  \___|  | (  <_> )  | \/\___  |
 \______  /___|  /\____/ \___  >____/|____(____  /__|  \___  >    \___  /  (____  /\___  >__|  \____/|__|   / ____|
        \/     \/            \/                \/          \/         \/        \/     \/                   \/
    """))
    cont()
    intro()


title_screen()
