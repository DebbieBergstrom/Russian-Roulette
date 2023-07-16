import random 

def random_chamber():
    """
    Randomizes a number from 1 to 6 which represents the 
    6 chambers in the cylinder of the revolover and one
    contains a bullet.
    """
    return random.randint(1, 6) != 3    #sets the third out of six chambers as the one with a bullet inside