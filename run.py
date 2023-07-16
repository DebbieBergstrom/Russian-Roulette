import random

def survives_spin():
    """
    Randomizes a number from 1 to 6 which represents the 
    6 chambers in the cylinder of the revolover and one
    contains a bullet. 5 out of 6 chance to survive = True
    """
    return random.randint(1, 6) != 1    #sets the first out of six chambers with the bullet = False

print(survives_spin())