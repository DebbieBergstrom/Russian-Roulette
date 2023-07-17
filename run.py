import random


def randomize_spin():
    """
    Randomizes a number from 1 to 6 which represents the 
    6 chambers in the cylinder of the revolver and one
    contains a bullet. 2-6 = survive = True
    """
    return random.randint(1, 6) != 1  # sets the first out of six chambers with the bullet
print(randomize_spin())

def game():
    print("Welcome to the game, a deadly dance of Russian Roulette. Are you the desperate victim, backed into a corner with only a slim chance of survival? Or are you the divine assassin, believing every pull of the trigger to be a judgement from God? The choice is yours. Welcome to the twilight world where morality meets mortality.")
print(game())

def rules():
    print("""Russian Roulette is a deadly game of chance. Here's how it works:

    - Choose if you want to be assassin or victim. 
    - A revolver with a single bullet is placed on the table.
    - The cylinder is spun, randomizing the position of the bullet.
    - The victim is forced to pull the trigger. 
    - If the gun fires the victim dies and the assassin has carried out divine judgement.
    - If the gun doesn't fire, the victim survives and the assassin walks away to carry out God's will another day.

    May fate be in your favor. 
    Play now?" Yes press(N) - No press(N)""")
print(rules())

character_choice = input("""Are you the victim or the assassin?
Victim press(V) - Assassin press(A)
See the Rules press(R)""")
print(character_choice())

play_again = input("""Play again?
Yes press(Y), No press(N)""")
print(play_again())

v_story = """Caught in the cruel grips of a notorious assassin for a debt you could never pay off, you are given a chilling choice: your life or a game. A game so simple, yet so deadly it's been feared for centuries - Russian Roulette. In the eerie silence of the room, your heart pounds as you reach for the gun. This might be your only chance to reclaim your freedom, or it might be your end. The answer lies in the hands of fate."
It's time to put the bullet in one of the chambers and spin the cylinder.
Press (s) to spin"""

a_story = """You're known not just as an assassin, but as an arbiter of divine justice. Your method? Russian Roulette. In this fatal game, you believe it's not you, but the hand of God who pulls the trigger. Your victims are not just targets, they are sinners - a single name, a single debt, a single chance at redemption. 
It's time to put the bullet in one of the chambers and spin the cylinder.
Press (S) to spin"""




"""
print("Cylinder is spun... Your life flashes before your eyes and you question yourself and how 
        you ended up here. Well, you don't have any choices but to do as you're told... Pull the trigger!")
print(randomize_spin())
def pull_trigger():
    survives_spin = True
    if survives_spin:
        print(f"You survived! Did you have an angel watching out for you? Freedom is at your feet...")
    else:
        print(f"You're dead! If you don't see the bright light you're supposed to walk towards, \
            it might get very hot soon, sinner! Too late to be sorry...")
print(pull_trigger())
"""
