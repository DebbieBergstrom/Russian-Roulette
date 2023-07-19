# STORY STRINGS and INPUT PROMTS #

def play_game():
    """
    Initial introduction message gets displayed for the user
    """
    slow_print(
    "Welcome to the game, a deadly dance of " +
    "\nRussian Roulette!\n" +
    "\nAre you the desperate victim, backed into " +
    "\na corner with only a slim chance of survival? Or " +
    "\nare you the divine assassin, believing every pull " +
    "\nof the trigger to be a judgement from God? " +
    "\nThe choice is yours.\n" +
    "\nWelcome to the twilight world where morality " +
    "\nmeets mortality.\n"
)


def display_rules():
    """
    Displays the rules
    """
    slow_print(
        "\nRussian Roulette is a deadly game of chance." +
        "\nHere's how it works:" +
        "\n" +
        "\n- Choose if you want to be assassin or victim." +
        "\n- Press one of the prompted keys to choose, then 'Enter'" +
        "\n- A revolver with a single bullet is placed on the table." +
        "\n- The cylinder is spun, randomizing the position of the bullet." +
        "\n- The victim is forced to pull the trigger." +
        "\n- If the gun fires -victim dies, the assassin has carried out divine judgement." +
        "\n- If the gun doesn't fire -victim survives, the assassin walks away" +
        "\n" +
        "\nMay fate be in your favor.\n"
    )


def get_character_choice():
    return validate_input(
        "\nAre you the victim or the assassin?" +
        "\n" +
        "\nVictim press(V) - Assassin press(A)" +
        "\nSee the Rules press(R)\n",
        ['v', 'a', 'r'],
        "\nOnly the provided options are valid. Choose one of them.\n"
    )


def get_story(character_choice):
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
        "\nIt's time to put the bullet in one of the chambers and spin the cylinder...\n")
            if character_choice == 'v'
            # Story if the user choose 'Assassin'
            else ("You're known not just as an assassin, but as an arbiter " +
        "\nof divine justice. Your method? Russian Roulette. In this fatal " +
        "\ngame, you believe it's not you, but the hand of God who pulls " +
        "\nthe trigger. Your victims are not just targets, they are " +
        "\nsinners - a single name, a single debt, a single chance at " +
        "\nredemption." +
        "\n" +
        "\nIt's time to put the bullet in one of the chambers and spin the cylinder...\n")
    )           


def get_result_message(character_choice, survival_result):
    if character_choice == 'v':
        message =(
        # Victims survival message
        ("\nYou survived!\nDid you have an angel watching out for " +
        "\nyou? Freedom is at your feet...\n")
            if survival_result
            # Victims death message
            else (
            "\nYou're dead!\nIf you don't see the bright light " +
            "\nyou're supposed to walk towards, it might get very hot in purgatory " +
            "\nsoon, sinner! Too late to be sorry...\n")
        )
    else:
        message = (
            # Assassins message that victim survived
            ("\nVictim survived!\nGod must have a greater plan! Let's find " +
            "\nanother sinner and test his faith.\n")
            if survival_result
            # Assassins message that victim died
            else ("\nVictim's dead!\nWith a clear conscience you just sent " +
            "\nthe poor victim's soul to the eternal flames in purgatory.\n" +
            "\nLet's find another sinner and test their faith.\n")
        )
    return message

def ask_play_now_or_quit():
    """
    Ask player if they want to play or quit.
    If 'yes', clears screen and return True.
    I 'no', prints end message and quit the game.
    """
