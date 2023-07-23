import random
import os
import sys
import time
from ascii import (
    gun_fires,
    welcome_art,
    cylinder_spun_victim_message,
    cylinder_spun_assassin_message,
    you_died,
    victim_died
    you_survived,
    victim_survived
)

# GAME FUNCTIONS


def randomize_spin(bullets):
    """
    Randomizes a number from 1 to 6 which represents the 6 chambers in the
    cylinder of the revolver.Depending on the difficulty, 1, 2, or 3 chambers
    contain a bullet. If the randomized number is within the bullet range,
    returns False (indicating that the player is shot)
    If the randomized number is outside the bullet range, returns True
    (indicating that the player survived)
    """
    return random.randint(1, 6) > bullets


def slow_print(string, delay=0.01):
    """
    Delays string printing for smooth print effect.
    """
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_input(string, delay=0.02):
    """
    Delays input prompt printing for smooth print effect
    """
    slow_print(string, delay)
    return input().lower()


def validate_input(promt, valid_inputs, error_message):
    """
    Function that holds promt, delay printing + error message
    for validation of user inputs.
    """
    while True:
        user_input = slow_input(promt)
        if user_input in valid_inputs:
            return user_input
        else:
            slow_print(error_message)


# STORY STRINGS and INPUT PROMTS #

def play_game():
    """
    Initial introduction message gets displayed for the user
    with ASCII art of a revolver.
    """
    welcome_art()
    time.sleep(3)
    slow_print(
        "\n" +
        "\nAre you the desperate victim, backed into " +
        "\na corner with only a slim chance of survival? Or " +
        "\nare you the divine assassin, believing every pull " +
        "\nof the trigger to be a judgement from God? " +
        "\nThe choice is yours." +
        "\nWelcome to the twilight world where morality " +
        "\nmeets mortality.\n"
    )


def display_rules():
    """
    Displays the rules
    """
    os.system('clear')

    slow_print(
        "\nRussian Roulette is a deadly game of chance." +
        "\nHere's how it works:" +
        "\n" +
        "\n- Choose if you want to be assassin or victim." +
        "\n- Choose the level of difficulty of the game. " +
        "\n- Press one of the prompted keys whenyou choose, then 'Enter'" +
        "\n- A revolver with 1, 2 or 3 bullets is loaded." +
        "\n- The cylinder is spun, randomizing the position of the bullets." +
        "\n- The victim is forced to pull the trigger." +
        "\n- If the gun fires -victim dies and divine judgement prevails." +
        "\n- If the gun doesn't fire -victim lives, the assassin walks away" +
        "\n" +
        "\nMay fate be in your favor.\n"
    )


def get_character_choice():
    """
    Asks player which character they want to play
    """
    return validate_input(
        "\nAre you the victim or the assassin?" +
        "\n" +
        "\nVictim press(V) - Assassin press(A)" +
        "\nSee the Rules press(R)\n",
        ['v', 'a', 'r'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )


def get_story(character_choice):
    """
    Displays the story that's tied to the chosen character.
    """
    os.system('clear')

    return (
        # Story if the user choose 'Victim'
        ("\nCaught in the cruel grips of a notorious assassin for a debt " +
         "\nyou could never pay off, you are given a chilling choice: your " +
         "\nlife or a game. A game so simple, yet so deadly it's been " +
         "\nfeared for centuries - Russian Roulette. In the eerie silence " +
         "\nof the room, your heart pounds as you reach for the gun. This " +
         "\nmight be your only chance to reclaim your freedom, or it might " +
         "\nbe your end. The answer lies in the hands of fate." +
         "\n" +
         "\nIt's time to put bullets in the chambers " +
         "\nand spin the cylinder...\n")
        if character_choice == 'v'
        # Story if the user choose 'Assassin'
        else (
            "\nYou're known not just as an assassin, but as an arbiter " +
            "\nof divine justice. Your method? Russian Roulette. In this " +
            "\nfatal game, you believe it's not you, but the hand of God " +
            "\nwho pulls the trigger. Your victims are not just targets, " +
            "\nthey are sinners - a single name, a single debt, a single " +
            "\nchance at redemption." +
            "\n" +
            "\nIt's time to put bullets in the chambers " +
            "\nand spin the cylinder...\n")
    )


def get_difficulty_level_for_victim():
    """
    Ask the victim for the difficulty level they want to play on, based on
    their self-perceived guilt.
    If 'Not so guilty', return 1.
    If 'Somewhat guilty', return 2.
    If 'Pretty guilty', return 3.
    """
    time.sleep(3)

    slow_print(
        "\nYou've been injected with truth serum and you're now incapable " +
        "\nof lying. Just how guilty are you? Choose the appropriate " +
        "\ndifficulty level for this round of Russian Roulette..." +
        "\n" +
        "\nKind of Not Guilty - Level Easy, has One bullet in the cylinder. " +
        "\nPress (1)\n" +
        "\nSomewhat Guilty - Level Medium, has Two bullets in the cylinder. " +
        "\nPress (2)\n" +
        "\nPretty Guilty - Level Hard, has Three bullets in the cylinder. " +
        "\nPress (3)\n"
    )

    guilt_level = validate_input(
        "",
        ['1', '2', '3'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )

    return int(guilt_level)


def get_difficulty_level_for_assassin():
    """
    Ask the assassin for the difficulty level they want to play on, based on
    their perception of the victim's guilt.
    If 'Not so guilty', return 1.
    If 'Somewhat guilty', return 2.
    If 'Pretty guilty', return 3.
    """
    time.sleep(3)

    slow_print(
        "\nYou have injected a truth serum into the victim and no lies " +
        "\nshould now be told. How guilty do you think he is? Choose the " +
        "\nappropriate difficulty level for this round of " +
        "\nRussian Roulette...\n"
        "\n" +
        "\nKind of Not Guilty - Level Easy, has One bullet in the cylinder. " +
        "\nPress (1)\n" +
        "\nSomewhat Guilty - Level Medium, has Two bullets in the cylinder. " +
        "\nPress (2)\n" +
        "\nPretty Guilty - Level Hard, has Three bullets in the cylinder. " +
        "\nPress (3)\n"
    )

    guilt_level = validate_input(
        "",
        ['1', '2', '3'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )

    return int(guilt_level)


def ask_spin_cylinder():
    """
    Asks the player to spin the cylinder
    """
    os.system('clear')

    validate_input(
        "\nGun's loaded!\nPress (s) to spin the cylinder...\n",
        ['s'],
        "Only (s) is valid. There's no turning back...\n"
    )


def get_spin_story(character_choice):
    """
    Displays the story that's tied to the spinning of the cylinder.
    """
    slow_print(
        '''  
           _   '    '  _         
.  .  .  _) /)//)/)//)(/.  .  .  
           /         _/          
    '''
    )
    time.sleep(3)
    os.system('clear')

    return (
        # Victim's story when 'S' is pressed
        cylinder_spun_victim_message()
        if character_choice == 'v'
        # Assassin's story when 'S' is pressed
        else
        cylinder_spun_assassin_message()
    )


def ask_pull_trigger():
    """
    Asks the player to pull the trigger
    """
    time.sleep(3)
    validate_input(
        "\nPull the trigger! Press (enter)\n",
        [''],
        "\nDon't extend the suffering. Press only (enter)\n"
    )


def get_result_message(character_choice, survival_result):
    """
    Displays the survival/death message that's tied to
    the chosen character.
    """
    os.system('clear')
    gun_fires()
    time.sleep(5)
    os.system('clear')

    if character_choice == 'v':
        if survival_result:
            ascii_art = you_survived()
            message = (
                ascii_art + "\n" +
                "\nDude, relax, the gun just clicked. You survived! " +
                "\nDid you have an angel watching out for " +
                "\nyou? Freedom is at your feet...\n")
        else:
            ascii_art = you_died()
            message = (
                ascii_art + "\n" +
                "\nIf you don't see the bright light " +
                "\nyou're supposed to walk towards, it might get very " +
                "\nhot soon, sinner! Too late to be sorry... " +
                "\nPurgatory awaits!\n")
    else:
        if survival_result:
            ascii_art = victim_survived()
            message = (
                ascii_art + "\n" +
                "\nYou were kinda expecting a BOOM, but the gun just " +
                "\nclicked... Guess God has a greater plan! " +
                "\nLet's find another sinner and test his faith.\n")
        else:
            ascii_art = victim_died()
            message = (
                ascii_art + "\n" +
                "\nWith a clear conscience you just sent " +
                "\nthe poor victim's soul to the eternal flames " +
                "\nin purgatory.\n" +
                "\nLet's find another sinner and test their faith.\n")
    return message


def ask_play_now_or_quit():
    """
    Ask player if they want to play now or not.
    If 'yes', clears screen and return True.
    If 'no', prints end message and quit the game.
    """
    play_now = validate_input(
        "\nPlay now?" +
        "\nYes press(Y), No press(N)\n",
        ['y', 'n'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )

    # If yes, player is taken back to play again
    if play_now == "y":
        os.system('clear')
        return True

    # If no, player gets notified before the game ends
    elif play_now == "n":
        slow_print("\nWelcome back! Game ends...")
        time.sleep(2)
        os.system('clear')
        sys.exit()


def ask_play_again_or_quit():
    """
    Ask player if they want to play again or not.
    If 'yes', clears screen and return True.
    If 'no', prints end message and quit the game.
    """
    play_again = validate_input(
        "\nPlay again?" +
        "\nYes press(Y), No press(N)\n",
        ['y', 'n'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )

    # If yes, player is taken back to play again
    if play_again == "y":
        slow_print("\nAwesome! Let's test your fate again!")
        time.sleep(2)
        os.system('clear')
        return True

    # If no, player gets notified before the game ends
    elif play_again == "n":
        slow_print(
            "\nNuff action for today, huh. See you next time!\nGame ends...")
        time.sleep(2)
        sys.exit()
