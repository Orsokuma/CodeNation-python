import random
player = {
    "riddles": 0,
    "points": 0
}
class code:
    debug = True

class text_formatting:
    purple = '\033[95m'
    yellow = '\033[1;33;40m'
    black = '\033[1;33;30m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    orange = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    reset = '\033[0m'
def typing_effect(content):
    print(content)

def riddles():
    global player
    riddles = {
        0: {
            "question": "I go around in circles, but always straight ahead. I never complain no matter where I am led. What am I?",
            "answers": ["a wheel", "wheel", "wheels", "horse", "a mule", "mule", "donkey", "a donkey"]
        },
        1: {
            "question": "What has hands, but cannot clap?",
            "answers": ["a clock", "clock", "clocks", "the clock", "the clocks", "butt cheeks"]
        },
        2: {
            "question": "What has a head and a tail, but no body?",
            "answers": ["a coin", "coin", "coins"]
        },
        3: {
            "question": "What has many keys, but can't open a single lock?",
            "answers": ["a piano", "piano", "a keyboard", "keyboard"]
        },
        4: {
            "question": "What can you break, even if you never pick it up or touch it?",
            "answers": ["a promise", "promise", "a heart", "heart", "your heart", "trust", "sanity", "word", "your word"]
        },
        5: {
            "question": "What goes up, but never comes down?",
            "answers": ["your age", "age"]
        }
    }
    used = []
    riddle_count = len(riddles)
    while player["riddles"] < riddle_count-1:
        filtered_riddles = {key: riddles for key in riddles if key not in used}
        if code.debug == True:
            print(f"{text_formatting.red} FILTERED: {filtered_riddles}{text_formatting.reset}\n")
        index = random.randint(0, len(filtered_riddles)-1)
        used.append(index)
        riddle = filtered_riddles[0][index]
        if code.debug == True:
            print(f"{text_formatting.red} SELECTED: {riddle}{text_formatting.reset}\n")

        typing_effect(riddle["question"])
        response = input("\nResponse:\n")
        if response.lower().strip() in riddle["answers"]:
            player["riddles"] += 1
            # award_points()
            extra = "" if index > riddle_count or player["riddles"] >= 3 else " The next riddle is.."
            typing_effect(f"Very good.{extra}\n")
        else:
            # dock_points()
            typing_effect("Incorrect!\n")
        index += 1
        if index >= riddle_count:
            break
    return True if player["riddles"] >= 3 else False

do_riddle = False
while do_riddle == False:
    do_riddle = riddles()