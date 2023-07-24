from termcolor import colored, cprint

def gun_fires():
    """
    Displays ASCII art a BOOM indicating that the gun
    has been fired.
    """
    cprint(
    ''' 
    $$$$$$$\   $$$$$$\   $$$$$$\  $$\      $$\ $$\ 
    $$  __$$\ $$  __$$\ $$  __$$\ $$$\    $$$ |$$ |
    $$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$\  $$$$ |$$ |
    $$$$$$$\ |$$ |  $$ |$$ |  $$ |$$\$$\$$ $$ |$$ |
    $$  __$$\ $$ |  $$ |$$ |  $$ |$$ \$$$  $$ |\__|
    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |    
    $$$$$$$  | $$$$$$  | $$$$$$  |$$ | \_/ $$ |$$\ 
    \_______/  \______/  \______/ \__|     \__|\__|
    '''
    , 'red')


def welcome_art():
    """
    ASCII art displayed at the very beginning of game
    with welcome text.
    """
    cprint(''' 
            ,___________________________________________/7_ 
           |-_______------. `\                             |
       _,/ | _______)     |___\____________________________|
  .__/`((  | _______      | (/))_______________=.
     `~) \ | _______)     |   /----------------_/
       `__y|______________|  /
       / ________ __________/
      / /#####\(  \  /     ))
     / /#######|\  \(     //
    / /########|.\______//`
   / /###(\)###||`------``
  / /##########||	Welcome to the game, 
 / /###########||	 a deadly dance of
( (############||	  Russian Roulette!
 \ \####(/)####))
  \ \#########//
   \ \#######//
    `---|_|--`\n''', 'yellow')


def cylinder_spun_victim_message():
    """
    Displays ASCII art of a revolver cylinder being pointed in front
    of you along with a suspenseful message for the victim.
    """
    cprint(
    '''
      .--.      .-'.      .--.      .--.      .--.      .--.      .`-.     
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      
          ^         
         | |        
       @#####@      
     (###   ###)-.  
   .(###     ###) \\ 
  /  (###   ###)   )
 (=-  .@#####@|_--"   Cylinder is spun... Your life flashes
 /\\    \\_|l|_/ (\\  before your eyes and you question
(=-\\     |l|    /    yourself and how you ended up here.
 \\  \\.___|l|___/    Well, you don't have any choices
 /\\      |_|   /     but to do as you're told...
(=-\\._________/\\    
 \\             /    
   \\._________/     
     #  ----  #     
     #   __   #       
     \\########/      
         V
           .--.      .-'.      .--.      .--.      .--.      .--.      .`-. 
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--' 
    '''
    , 'blue')


def cylinder_spun_assassin_message():
    """
    Displays ASCII art of a revolver cylinder being pointed in front
    of you along with a suspenseful message for the assassin.
    """
    cprint(
    '''
      .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      
          ^         
         | |        
       @#####@      
     (###   ###)-.  
   .(###     ###) \\ 
  /  (###   ###)   )
 (=-  .@#####@|_--"   Cylinder is spun... As you place
 /\\    \\_|l|_/ (\\  the revolver on the table, you feel
(=-\\     |l|    /    the familiar rush of adrenaline. Is this
 \\  \\.___|l|___/    another soul destined for salvation
 /\\      |_|   /     or damnation? The answer lies in the 
(=-\\._________/\\    hands of fate...
 \\             /    
   \\._________/     
     #  ----  #     
     #   __   #       
     \\########/      
         V
 .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.
:::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.
'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'       
    '''
    , 'blue')


def you_died():
    """
    Displays ASCII art of a message indicating the player died.
    """
    # Each color section is defined as a separate string
    yellow_part = colored('''
     )    )           (     (        (       ____ 
  ( /( ( /(           )\ )  )\ )     )\ )   |   / ''', 'yellow')

    magenta_part = colored('''
  )\()))\())     (   (()/( (()/( (  (()/(   |  /  
 ((_)\((_)\      )\   /(_)) /(_)))\  /(_))  | /   ''', 'magenta')

    red_part = colored('''
__ ((_) ((_)  _ ((_) (_))_ (_)) ((_)(_))_   |/    
\ \ / // _ \ | | | |  |   \|_ _|| __||   \ (      
 \ V /| (_) || |_| |  | |) || | | _| | |) |)\     
  |_|  \___/  \___/   |___/|___||___||___/((_)    ''', 'red')  

    return yellow_part + magenta_part + red_part


def victim_died():
    """
    Displays ASCII art of a message indicating the victim died.
    """
    # Each color section is defined as a separate string
    yellow_part = colored('''
        (               (      *      (    (      (      ____ 
        )\ )  (    *   ))\ ) (  `     )\ ) )\ )   )\ )  |   / ''', 'yellow')

    magenta_part = colored('''
 (   ( (()/(  )\ ` )  /(()/( )\))(   (()/((()/(( (()/(  |  /  ''', 'magenta')

    red_part = colored('''
 )\  )\ /(_)|((_) ( )(_))(_)|(_)()\   /(_))/(_))\ /(_)) | /   
((_)((_|_)) )\___(_(_()|_)) (_()((_) (_))_(_))((_|_))_  |/    
\ \ / /|_ _((/ __|_ _||  \/  |  |   \_ _| __|   \(      
 \ V /  | | | (__  | |  | | | |\/| |  | |) | || _|| |) )\     
  \_/  |___| \___| |_| |___||_|  |_|  |___/___|___|___((_)''', 'red')  

    return yellow_part + magenta_part + red_part


def you_survived():
    """
    Displays ASCII art of a message indicating the player has survived.
    """
    return colored(
    """
    __  __               _____                  _                ____
    \ \/ /___  __  __   / ___/__  ________   __(_)   _____  ____/ / /
     \  / __ \/ / / /   \__ \/ / / / ___/ | / / / | / / _ \/ __  / / 
     / / /_/ / /_/ /   ___/ / /_/ / /   | |/ / /| |/ /  __/ /_/ /_/  
    /_/\____/\__,_/   /____/\__,_/_/    |___/_/ |___/\___/\__,_(_)   
    """
    , 'green')


def victim_survived():
    """
    Displays ASCII art of a message indicating the victim has survived.
    """
    return colored( 
    """
   _____                  _                ____
  / ___/__  ________   __(_)   _____  ____/ / /
  \__ \/ / / / ___/ | / / / | / / _ \/ __  / / 
 ___/ / /_/ / /   | |/ / /| |/ /  __/ /_/ /_/  
/____/\__,_/_/    |___/_/ |___/\___/\__,_(_)
    """
    , 'green')

def injection():
    """
    Art showing a syringe to add to the story where victim
    gets injected with truth serum.
    """
    cprint(
    """
      |___________________________________
|-----|- - -|''''|''''|''''|''''|''''|'**\\|__
|- -  |  cc 6    5    4    3    2    1 *** __]==--------------
|-----|________________________________**/|
'     |````````````````````````````````````
    """
    , 'light_green')


