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
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_input(string, delay=0.02):
    slow_print(string, delay)
    return input().lower()


def validate_input(promt, valid_inputs, error_message):
    while True:
        user_input = slow_input(promt)
        if user_input in valid_inputs:
            return user_input
        else:
            slow_print(error_message)


def game():
    """
    Introduction message gets displayed for the user
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

    # main game loop
    while True:
        character_choice = validate_input(
            """Are you the victim or the assassin?
            Victim press(V) - Assassin press(A)
            See the Rules press(R)\n""",
            ['v', 'a', 'r'],
            "Only the provided options are valid. Choose one of them.\n"
        )

        # Takes user back to start of the game
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

            # Takes user back to start of the game or ends game
            play_now = slow_input("""Play now?
            Yes press(Y), No press(N)\n""")

            if play_now == "y":
                os.system('clear')
                continue

            elif play_now == "n":
                break

        # If the user choose 'Victim'
        if character_choice in ["v", "a"]:
            story = (
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
                else """You're known not just as an assassin, but as an arbiter
            of divine justice. Your method? Russian Roulette. In this fatal
            game, you believe it's not you, but the hand of God who pulls
            the trigger. Your victims are not just targets, they are
            sinners - a single name, a single debt, a single chance at
            redemption.\n It's time to put the bullet in one of the
            chambers and spin the cylinder...\n"""
            )
            slow_print(story)

            slow_input("Press (s) to spin\n")

            story_spin = (
                """Cylinder is spun... Your life flashes before your eyes and
                you question yourself and how you ended up here. Well, you
                don't have any choices but to do as you're told..."""
                if character_choice == 'v'
                else """Cylinder is spun... As you place the revolver on the
                table, you feel the familiar rush of adrenaline. Is this
                another soul destined for salvation or damnation? The answer
                lies in the hands of fate.\n"""
            )
            slow_print(story_spin)

            pull_trigger = slow_input("Pull the trigger! Press (enter)\n")

            survival_result = randomize_spin()

            if character_choice == 'v':
                message = (
                    """You survived! Did you have an angel watching out for
                    you? Freedom is at your feet..."""
                    if survival_result
                    else """You're dead! If you don't see the bright light
                    you're supposed to walk towards, it might get very hot
                    soon, sinner! Too late to be sorry..."""
                )
            else:
                message = (
                    """Victim survived! God must have a greter plan! Let's find
                    another sinner and test his faith."""
                    if survival_result
                    else """Victim's dead! With a clear concience you just sent
                    the poor victim's soul to the eternal flames in purgatory.
                    Let's find another sinner and test their faith."""
                )

            slow_print(message)

            # Takes user back to start of the game
            play_again = slow_input("""Play again?
            Yes press(Y), No press(N)\n""")

            if play_again == "y":
                os.system('clear')
                continue

            elif play_again == "n":
                break


print(game())