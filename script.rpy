# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Garnet")
define a = Character("Amethyst")

image Garnet:
    "garnet.png"
    zoom 1.3

image Amethyst:
    "amethyst.png"
    zoom 1.8

image Cookie_cat:
    "cookie_cat.png"

default rock_paper_scissors = ["rock", "paper", "scissors"]
# The game starts here.

label game_start:
        a "Alright Steven, let's start."
        a "Rock"
        a "Paper"
        a "Scissors"
        a "Shoot!"
        menu:
            "Rock":
                call play_rock_paper_scissors("rock")
            "Paper":
                call play_rock_paper_scissors("paper")
            "Scissors":
                call play_rock_paper_scissors("scissors")
        menu:
            "Play again":
                jump game_start
            "End game":
                return



label play_rock_paper_scissors(choice):
    $ player_choice = choice
    $ Amethyst_choice = renpy.random.choice(rock_paper_scissors)

    if player_choice == Amethyst_choice:
        a "[Amethyst_choice]!"
        a "It's a tie!"
        return          

    elif (player_choice == "rock" and Amethyst_choice == "paper") or (player_choice == "paper" and Amethyst_choice == "scissors") or (player_choice == "scissors" and Amethyst_choice == "rock"):
        a "[Amethyst_choice]!"
        a "I win!"
        return

    elif (player_choice == "rock" and Amethyst_choice == "scissors") or (player_choice == "paper" and Amethyst_choice == "rock") or (player_choice == "scissors" and Amethyst_choice == "paper"):
        a "[Amethyst_choice]!"
        a "You win!"
        return
    

label start:

    scene bg room

    show Garnet

    g "Steven you need to stay here with amethyst."
    g " Me and Pearl are going on a mission."
    g "Stay safe and have fun."

    hide Garnet 

    show Amethyst

    a "Hey Steven!"
    a "Looks like I'm stuck with you for you for a while."
    a "What do you want to do?"
    menu:
        "Play a game":
                a "Cool, let's play rock paper scissors."
                call game_start
                a "Good Game Steven!"
                label Gems_Back_Home:
                hide Amethyst
                show Garnet
                g "Hey Steven we're back."
                g "Did you have fun with Amethyst?"
                menu:
                    "Yes, we had fun!":
                        g "Glad to hear."
                        hide Garnet
                        show Amethyst
                        a "Yeah, I'm a pretty good babysitter."
                        return
                    "No, it was boring.":
                        hide Garnet
                        show Amethyst
                        a "wHaT? Come on Steven!"
                        a "Next time you can stay with Pearl instead."
                        return

        "Eat some food":
            a "Great! How do cookie cats sound?"
            menu:
                "No, I'm not hungry":
                    a "Let's play a game instead."
                    a "We can play rock paper scissors."
                    call game_start
                    a "Good Game Steven!"
                    call Gems_Back_Home
                "Yes, that sounds great!":
                    a "Great I'll grab some for us."
                    hide Amethyst
                    pause 3.0
                    show Amethyst
                    show Cookie_cat
                    a "Here Steven, enjoy!"
                    hide Cookie_cat
                    pause 2.0
                    a "So, how was it?"
                    menu:
                        "That was delicious thanks!":
                            a "You're welcome Steven!"
                            a "Mine was pretty good too!"
                            call Gems_Back_Home                       
                        "I didn't like it.":
                            a "Oh, sorry Steven."
                            a "Maybe you got a bad one."
                            call Gems_Back_Home
    # This ends the game.

    return
