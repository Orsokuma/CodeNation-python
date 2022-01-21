from random import choice
def rock_paper_scissors():
    global player
    # Basic player data
    player = {
        "step": 1,
        "rps": {
            "wins": 0,
            "losses": 0,
            "draws": 0
        }
    }

    # Return an "s" (or "es") if num != 1
    def pluralize(num, with_e = False):
        return "" if num == 1 else ("es" if with_e == True else "s")

    # Output the current scores
    def get_rps_score():
        # PHP's sprintf() -> Python equivalent, output scores as formatted
        return "%d win%s :: %d loss%s :: %d draw%s" % (
            player["rps"]["wins"],
            pluralize(player["rps"]["wins"]),
            player["rps"]["losses"],
            pluralize(player["rps"]["losses"], True),
            player["rps"]["draws"],
            pluralize(player["rps"]["draws"])
        )

    # We support short-form guesses! So, relate them to what they represent
    def get_formatted_answer(guess):
        conv = {
            "r": "rock",
            "p": "paper",
            "s": "scissors",
        }
        # Return relative response if short-form, or the full guess if given
        return conv[guess] if guess not in ["rock", "paper", "scissors"] else guess

    # If the round was won
    def rps_win(guess, outcome):
        global player
        player["rps"]["wins"] += 1
        print(f"You chose {get_formatted_answer(guess)} and your opponent played {get_formatted_answer(outcome)} · you win this round. {get_rps_score()}")

    # If the round was lost
    def rps_lose(guess, outcome):
        global player
        player["rps"]["losses"] += 1
        print(f"You chose {get_formatted_answer(guess)} and your opponent played {get_formatted_answer(outcome)} · you lose this round. {get_rps_score()}")

    # If the round was a draw
    def rps_draw(guess):
        global player
        player["rps"]["draws"] += 1
        print(f"Both you and your opponent chose {get_formatted_answer(guess)} · you drew this round. {get_rps_score()}")

    # Reset the player metrics
    def rps_reset():
        global player
        player["rps"]["wins"] = player["rps"]["losses"] = player["rps"]["draws"] = 0


    def rock_paper_scissors(guess):
        # set permissable outputs
        opts = ["rock", "paper", "scissors"]
        # convert to lowercase for easier string comparisons
        guess = guess.lower()
        # if whatever the user guessed isn't in opts or the short-form answers
        if guess not in (opt.lower() for opt in opts) and guess not in ["r", "p", "s"]:
            # tell 'em!
            print("That's not a valid option. Please enter either rock, paper or scissors")
        # Pick a random opt
        rand_opt = choice(opts)
        # GUESS: PAPER
        if guess in ["paper", "p"]:
            if rand_opt == "rock":
                # paper beats rock
                print(rps_win(guess, rand_opt))
            elif rand_opt == "scissors":
                # scissors beats paper
                print(rps_lose(guess, rand_opt))
            else:
                # paper draws against paper
                print(rps_draw(guess))
        # GUESS: ROCK
        elif guess in ["rock", "r"]:
            if rand_opt == "scissors":
                # rock beats scissors
                print(rps_win(guess, rand_opt))
            elif rand_opt == "paper":
                # paper beats rock
                print(rps_lose(guess, rand_opt))
            else:
                # rock draws against rock
                print(rps_draw(guess))
        # GUESS: SCISSORS
        elif guess in ["scissors", "s"]:
            if rand_opt == "paper":
                # scissors beats paper
                print(rps_win(guess, rand_opt))
            elif rand_opt == "rock":
                # rock beats scissors
                print(rps_lose(guess, rand_opt))
            else:
                # scissors draws against scissors
                print(rps_draw(guess))
        else:
            # Oi! Put somethin' right or don't bother!
            print("You didn't select a valid option")
    # Reset player metrics for first run
    rps_reset();
    # If the player hasn't won or lost yet
    while player["rps"]["wins"] < 3 and player["rps"]["losses"] < 3:
        # Take a guess!
        guess = input("Rock, Paper, or Scissors?\n")
        # Call the game and pass the guess as an argument
        rock_paper_scissors(guess)

# Finally, run the entire script
rock_paper_scissors();