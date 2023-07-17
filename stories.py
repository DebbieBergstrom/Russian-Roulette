######## STORY STRINGS and INPUT PROMTS ########

welcome = """Welcome to the game, a deadly dance of Russian Roulette. Are you the desperate victim, backed into a corner with only a slim chance of survival? Or are you the divine assassin, believing every pull of the trigger to be a judgement from God? The choice is yours. Welcome to the twilight world where morality meets mortality."""

# User chooses if they want to be 'Victim' or 'Assassin'.
character_choice = input("""Are you the victim or the assassin?
Victim press(V) - Assassin press(A)
See the Rules press(R)\n""")

# Game rules
rules = """Russian Roulette is a deadly game of chance. Here's how it works:

    - Choose if you want to be assassin or victim. 
    - A revolver with a single bullet is placed on the table.
    - The cylinder is spun, randomizing the position of the bullet.
    - The victim is forced to pull the trigger. 
    - If the gun fires the victim dies and the assassin has carried out divine judgement.
    - If the gun doesn't fire, the victim survives and the assassin walks away to carry out God's will another day.

    May fate be in your favor."""

# Takes user back to start of the game
play_now = input("""Play now?
Yes press(Y), No press(N)\n""")

# Story displayed when user choose to be the 'Victim'
v_story = """Caught in the cruel grips of a notorious assassin for a debt you could never pay off, you are given a chilling choice: your life or a game. A game so simple, yet so deadly it's been feared for centuries - Russian Roulette. In the eerie silence of the room, your heart pounds as you reach for the gun. This might be your only chance to reclaim your freedom, or it might be your end. The answer lies in the hands of fate."
It's time to put the bullet in one of the chambers and spin the cylinder.
Press (s) to spin"""

v_story_spin = """Cylinder is spun... Your life flashes before your eyes and you question yourself and how you ended up here. Well, you don't have any choices but to do as you're told..."""

# Story displayed when user choose to be the 'Assassin'
a_story = """You're known not just as an assassin, but as an arbiter of divine justice. Your method? Russian Roulette. In this fatal game, you believe it's not you, but the hand of God who pulls the trigger. Your victims are not just targets, they are sinners - a single name, a single debt, a single chance at redemption. 
It's time to put the bullet in one of the chambers and spin the cylinder.
Press (S) to spin"""

a_story_spin = """Cylinder is spun... As you place the revolver on the table, you feel the familiar rush of adrenaline. Is this another soul destined for salvation or damnation? The answer lies in the hands of fate."""

pull_trigger = input("Pull the trigger! Press (enter)\n")

# Takes user back to start of the game
play_again = input("""Play again?
Yes press(Y), No press(N)\n""")