import random

def randomize_spin():
    """
    Randomizes a number from 1 to 6 which represents the 
    6 chambers in the cylinder of the revolver and one
    contains a bullet. 5 out of 6 chance to survive = True
    """
    return random.randint(1, 6) != 1    #sets the first out of six chambers with the bullet = False

print("""Cylinder is spun... Your life flashes before your eyes and you question yourself and how 
        you ended up here. Well, you don't have any choices but to do as you're told... Pull the trigger!""")

print(randomize_spin())

def pull_trigger():
    survives_spin = True
    if survives_spin:
        print(f"You survived! Did you have an angel watching out for you? Freedom is at your feet...")
    else:
        print(f"You're dead! If you don't see the bright light you're supposed to walk towards, \
            it might get very hot soon, sinner! Too late to be sorry...")

print(pull_trigger())