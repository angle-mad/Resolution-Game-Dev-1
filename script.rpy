# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init python:
    import random
    bgm_tracks = [
    "I'm Still Here.mp3",
    "Lion's Theme.mp3",
    "Night Drive.mp3",
    "Rose's Room.mp3"
    ]

image bg room:
    "white_backgrnd.png"

default Happiness = 30
default win = 0
default play_rps = False

define g = Character("Garnet")
define a = Character("Amethyst", image="Amethyst")
image Garnet:
    "garnet.png"
    zoom 1.3

image Amethyst:
    "amethyst.png"
    zoom 1.8

image Amethyst_bored:
    "amethyst_bored.png"
    zoom 2.0

image Amethyst_up:
    "amethyst_hair_up.png"
    zoom 1.9

image Amethyst_fully_up:
    "amethyst_hair_fully_up.png"
    zoom 1.8

image Amethyst_down:
    "amethyst_hair_down.png"
    zoom 1.9

image Cookie_cat:
    "cookie_cat.png"

image the_bits:
    "the_bits.png"
    zoom 0.8

default rock_paper_scissors = ["rock", "paper", "scissors"]
# The game starts here.

label game_start:
        $ play_rps = True
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
        $ Happiness = Happiness - 5
        return

    elif (player_choice == "rock" and Amethyst_choice == "scissors") or (player_choice == "paper" and Amethyst_choice == "rock") or (player_choice == "scissors" and Amethyst_choice == "paper"):
        a "[Amethyst_choice]!"
        a "You win!"
        $ Happiness = Happiness + 5
        $ win += 1
        return
    
label Gems_Back_Home:
                hide Amethyst
                show Garnet
                g "Hey Steven we're back."
                g "Did you have fun with Amethyst?"
                menu:
                    "Yes, I feel like a winner." if win >= 10:
                        hide Garnet
                        show Amethyst
                        a "Yeah, you really did win a lot."
                        hide Amethyst
                        show Garnet
                        g "It's great that you did so well, I'd say you're almost good as me."
                        g "I know I beat Amethyst all the time."
                        hide Garnet
                        show Amethyst
                        a "Well that's not fair in the first place!"
                        a "You can see in the future!"
                        a "Anyways Steven, Good Game"
                        return
                    "Yes, I had a great time!" if Happiness >= 45:
                        g "Glad to hear."
                        g "Maybe we need to make Amethyst your permanent babysitter."
                        hide Garnet
                        show Amethyst
                        a "I don't know about permanent babysitter but-"
                        a "yeah, I'm a pretty good babysitter."
                        return
                    "It was ok":
                        hide Garnet
                        show Amethyst
                        a "wHaT? Come on Steven!"
                        a "I thought you had fun!?"
                        a "Next time you can stay with Pearl instead."
                        return
                    "No, I hated it." if Happiness <= 15:
                        hide Garnet
                        show Amethyst
                        if play_rps:
                            a "Yeah, you did lose a bit in rock paper scissors"
                        a "Sorry for that Steven"
                        a "Next time we can try something else"
                        return
label Other_Activity:
    a "Did you want to do something else?"
    menu: 
        "Let's play a game":
            a "Alright"
            a "We can play some rock paper scissors"
            call game_start
            return
        "No, I'm done for today":
            a "OK, that's fine"
            return


label start:
    scene bg room 
    $ selected_bgm = random.choice(bgm_tracks)
    play music selected_bgm fadein 1.0 loop
    show Garnet
    g "Steven you need to stay here with Amethyst."
    g "Me and Pearl are going on a mission."
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
                call Gems_Back_Home
        "Eat some food":
            a "Great! What do you want?"
            menu:
                "A Cookie Cat":
                    a "Great, I'll grab one for you."
                    hide Amethyst
                    $ renpy.pause(2.0, hard=True)
                    show Amethyst
                    show Cookie_cat
                    a "Here Steven, enjoy!"
                    hide Cookie_cat
                    $ renpy.pause(1.0, hard=True)
                    a "So, how was it?"
                    menu:
                        "It was delicious, thanks!":
                            a "You're welcome Steven!"
                            $ Happiness = Happiness + 10
                            call Other_Activity
                            call Gems_Back_Home                 
                        "I didn't like it.":
                            a "Oh, sorry Steven."
                            a "It did look kind of melted."
                            a "Maybe you got a bad one."
                            $ Happiness = Happiness - 10
                            call Other_Activity
                            call Gems_Back_Home
                "The BITS":
                    a "Alright, I remember we had some leftovers I can microwave."
                    stop music fadeout 2.0
                    hide Amethyst
                    play sound "microwave_begin.mp3"
                    $ renpy.pause(8.0, hard=True)
                    play sound "microwave_hum.mp3" volume 0.3
                    $ renpy.pause(0.5, hard=True) 
                    show Amethyst 
                    $ renpy.pause(5.0, hard=True)
                    hide Amethyst
                    show Amethyst_bored
                    $ renpy.pause(5.0, hard=True)
                    hide Amethyst_bored
                    show Amethyst_down
                    $ renpy.pause(3.0, hard=True)
                    hide Amethyst_down
                    show Amethyst_up
                    $ renpy.pause(1.0, hard=True)
                    hide Amethyst_up
                    show Amethyst_fully_up
                    $ renpy.pause(1.0, hard=True)
                    hide Amethyst_fully_up
                    show Amethyst_up
                    $ renpy.pause(1.0, hard=True)
                    hide Amethyst_up
                    show Amethyst_down
                    $ renpy.pause(5.0, hard=True)
                    play sound "microwave_end.mp3"
                    $ renpy.pause(1.5, hard=True)
                    hide Amethyst_down
                    show Amethyst
                    a "They're done!{nw=1.0}"
                    hide Amethyst
                    $ renpy.pause(7.0, hard=True)
                    show Amethyst
                    play music selected_bgm fadein 1.0 loop
                    show the_bits
                    a "Here Steven."
                    hide the_bits
                    $ renpy.pause(2.0, hard=True)
                    a "So, how are they?"
                    menu:
                        "They are perfect! Thanks!":
                            a "You're welcome Steven!"
                            a "Glad you like them!"
                            $ Happiness = Happiness + 10
                            call Other_Activity
                            call Gems_Back_Home
                        "They are a little soggy for my liking":
                            a "Oh, sorry Steven."
                            a "Maybe I can use an air fryer next time."
                            a "My bad."
                            $ Happiness = Happiness - 10
                            call Other_Activity
                            call Gems_Back_Home
                "I'm not hungry":
                    a "Not feeling hungry, huh."
                    a "Let's play a game instead."
                    a "We can play rock paper scissors."
                    call game_start
                    a "Good Game Steven!"
                    call Gems_Back_Home
    return
