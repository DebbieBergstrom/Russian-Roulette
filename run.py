import random

######## GAME FUNCTIONS ########

def randomize_spin():
    """
    Randomizes a number from 1 to 6 which represents the 
    6 chambers in the cylinder of the revolver and one
    contains a bullet. 2-6 = survive = True
    """
    return random.randint(1, 6) != 1  # sets the first out of six chambers with the bullet

print(randomize_spin())


def game():
    


print(game())



