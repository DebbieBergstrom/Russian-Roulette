import random
import os
import sys
import time

# GAME FUNCTIONS #

def randomize_spin():
    """
    Randomizes a number from 1 to 6 which
    represents the 6 chambers in the cylinder of the revolver and one
    contains a bullet. 2-6 = survive = True
    """
    return random.randint(1, 6) != 1  # no.1 is the bullet


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


def game():
    """
    Initial introduction message gets displayed for the user
    """
    slow_print(
        """Welcome to the game, a deadly dance of
        Russian Roulette. Are you the desperate victim, backed
        into a corner with only a slim chance of survival?
        Or are you the divine assassin, believing every pull
        of the trigger to be a judgement from God? The choice
        is yours. Welcome to the twilight world where morality
        meets mortality.\n"""
    )

    # Game starts with asking the player to choose character
    while True:
        character_choice = validate_input(
            """Are you the victim or the assassin?
            Victim press(V) - Assassin press(A)
            See the Rules press(R)\n""",
            ['v', 'a', 'r'],
            "Only the provided options are valid. Choose one of them.\n"
        )

        # Takes user to see the rules if wanted
        if character_choice == "r":
            slow_print("""Russian Roulette is a deadly game of chance.
            Here's how it works:

            - Choose if you want to be assassin or victim.
            - A revolver with a single bullet is placed on the table.
            - The cylinder is spun, randomizing the position of the bullet.
            - The victim is forced to pull the trigger.
            - If the gun fires -victim dies, the assassin has carried out
              divine judgement.
            - If the gun doesn't fire -victim survives, the assassin walks away

            May fate be in your favor.\n""")

            # Asks player if the want to play now or quit
            play_now = validate_input(
                """Play now?
                Yes press(Y), No press(N)\n""",
                ['y', 'n'],
                "Only the provided options are valid. Choose one of them.\n"
            )

            # If yes, player is taken back to play again
            if play_now == "y":
                os.system('clear')
                continue

            # If no, player gets notified before the game ends
            elif play_now == "n":
                slow_print("Welcome back! Game ends...")
                time.sleep(2)
                quit()

        
        if character_choice in ["v", "a"]:
            story = (
            # Story if the user choose 'Victim'
            """Caught in the cruel grips of a notorious assassin for a debt
            you could never pay off, you are given a chilling choice: your
            life or a game. A game so simple, yet so deadly it's been
            feared for centuries - Russian Roulette. In the eerie silence
            of the room, your heart pounds as you reach for the gun. This
            might be your only chance to reclaim your freedom, or it might
            be your end. The answer lies in the hands of fate.\n It's time
            to put the bullet in one of the chambers and spin
            the cylinder...\n"""
                if character_choice == 'v'
                # Story if the user choose 'Assassin'
                else """You're known not just as an assassin, but as an arbiter
            of divine justice. Your method? Russian Roulette. In this fatal
            game, you believe it's not you, but the hand of God who pulls
            the trigger. Your victims are not just targets, they are
            sinners - a single name, a single debt, a single chance at
            redemption.\n It's time to put the bullet in one of the
            chambers and spin the cylinder...\n"""
            )
            slow_print(story)

            # Forces playes to spin the cylinder with the bullet inside
            spin = validate_input(
                "Press (s) to spin\n",
                ['s'],
                "Only (s) is valid. There's no turning back...\n"
            )

            story_spin = (
                # Victim's story when 'S' is pressed
                """Cylinder is spun... Your life flashes before your eyes and
                you question yourself and how you ended up here. Well, you
                don't have any choices but to do as you're told..."""
                if character_choice == 'v'
                # Assassin's story when 'S' is pressed
                else """Cylinder is spun... As you place the revolver on the
                table, you feel the familiar rush of adrenaline. Is this
                another soul destined for salvation or damnation? The answer
                lies in the hands of fate...\n"""
            )
            slow_print(story_spin)

            # Pulls the trigger that leads to the survival_result below
            pull_trigger = validate_input(
                "Pull the trigger! Press (enter)\n",
                [''],
                "Don't extend the suffering. Press only (enter)\n"
            )

            # Determines if the bullet was shot or not
            survival_result = randomize_spin()

            if character_choice == 'v':
                message = (
                    # Victims survival message
                    """You survived! Did you have an angel watching out for
                    you? Freedom is at your feet..."""
                    if survival_result
                     # Victims death message
                    else """You're dead! If you don't see the bright light
                    you're supposed to walk towards, it might get very hot in purgatory
                    soon, sinner! Too late to be sorry..."""
                )
            else:
                message = (
                     # Assassins message that victim survived
                    """Victim survived! God must have a greater plan! Let's find
                    another sinner and test his faith."""
                    if survival_result
                     # Assassins message that victim died
                    else """Victim's dead! With a clear concience you just sent
                    the poor victim's soul to the eternal flames in purgatory.
                    Let's find another sinner and test their faith."""
                )

            slow_print(message)

            # Asks player if the want to play again or quit
            play_again = validate_input(
                """Play again?
                Yes press(Y), No press(N)\n""",
                ['y', 'n'],
                "Only the provided options are valid. Choose one of them.\n"
            )

            # If yes, player is taken back to play again
            if play_again == "y":
                slow_print("Awesome! Let's test your fate again!")
                time.sleep(2)
                os.system('clear')
                continue

            # If no, player gets notified before the game ends
            elif play_again == "n":
                slow_print("Nuff action for today, huh. See you next time! Game ends...")
                time.sleep(2)
                quit()


game()