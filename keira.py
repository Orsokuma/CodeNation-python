import random

def game_start():
    global play_again
    print("Welcome to the first game. We will be playing an old favourite.")
    print(
        """
╔═══╗        ╔╗      ╔═══╗                    ╔═══╗
║╔═╗║        ║║      ║╔═╗║                    ║╔═╗║
║╚═╝║╔══╗╔══╗║║╔╗    ║╚═╝║╔══╗ ╔══╗╔══╗╔═╗    ║╚══╗╔══╗╔╗╔══╗╔══╗╔══╗╔═╗╔══╗
║╔╗╔╝║╔╗║║╔═╝║╚╝╝    ║╔══╝╚ ╗║ ║╔╗║║╔╗║║╔╝    ╚══╗║║╔═╝╠╣║══╣║══╣║╔╗║║╔╝║══╣
║║║╚╗║╚╝║║╚═╗║╔╗╗    ║║   ║╚╝╚╗║╚╝║║║═╣║║     ║╚═╝║║╚═╗║║╠══║╠══║║╚╝║║║ ╠══║
╚╝╚═╝╚══╝╚══╝╚╝╚╝    ╚╝   ╚═══╝║╔═╝╚══╝╚╝     ╚═══╝╚══╝╚╝╚══╝╚══╝╚══╝╚╝ ╚══╝
                               ║║
                               ╚╝
              """
    )
    print("You will have 3 rounds to beat the games master ")
    play_again = 4
    def input_number(message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return user_input

    def game_1():
        global play_again
        rock = """
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """

        paper = """
            _______
        ---'   ____)____
                  ______)
                _______)
                _______)
        ---.__________)
        """

        scissors = """
            _______
        ---'   ____)____
                  ______)
            __________)
            (____)
        ---.__(___)
        """

        # Adding Game Images into a list
        game_images = [rock, paper, scissors]

        # Taking input from user choice
        user_choice = input_number(
            "What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissor. \n => "
        )
        if user_choice >= len(game_images) - 1:
            print("Invalid choice given")
            game_1()

        print("User Choice: ")

        # print game image by user choice
        print(game_images[user_choice])

        # random computer choice
        computer_choice = random.choice(game_images)
        computer_choice_index = game_images.index(computer_choice)
        print("Computer Choice: ")

        # print game image by computer choice
        print(computer_choice)

        while play_again > 0:
            play_again -= 1
            if play_again <= 0:
                print(
                    "You are a failure. May your family live in the shadow of your shame forevermore."
                )
                quit

            # rules in logic
            if user_choice == 1 and computer_choice_index == 3:
                print("You win! 🎉")
                play_again -= 1
                game_1()
            elif computer_choice_index == 1 and user_choice == 3:
                print("You lose.  ☠")
                play_again -= 1
            elif computer_choice_index > user_choice:
                print("You lose. ☠")
                play_again -= 1
                game_1()
            elif user_choice > computer_choice_index:
                print("You win!🎉 ")
                game_1()
            elif computer_choice_index == user_choice:
                print("It's a draw.")
                play_again -= 1
                game_1()
            else:
                print("You typed an invalid number, You Lose.  ☠")
                print("Failure")
                quit

    game_1()

game_start()