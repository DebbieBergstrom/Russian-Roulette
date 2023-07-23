from termcolor import colored, cprint
from ascii import (
    gun_fires,
    welcome_art,
    cylinder_spun_victim_message,
    cylinder_spun_assassin_message,
    you_died,
    victim_died,
    you_survived,
    victim_survived,
    injection
)
from all_functions import (
    play_game,
    display_rules,
    get_character_choice,
    get_story,
    get_result_message,
    ask_play_now_or_quit,
    ask_play_again_or_quit,
    ask_spin_cylinder,
    ask_pull_trigger,
    randomize_spin,
    slow_print,
    slow_input,
    validate_input,
    get_spin_story,
    get_difficulty_level_for_victim,
    get_difficulty_level_for_assassin
)


def main():
    """
    Initializes the Russian Roulette Game
    """
    while True:
        play_game()
        character_choice = get_character_choice()

        # Takes user to see the rules if wanted
        if character_choice == "r":
            display_rules()
            if not ask_play_now_or_quit():
                continue

        elif character_choice in ["v", "a"]:
            story = get_story(character_choice)
            slow_print(story)
            if character_choice == 'v':
                bullets = get_difficulty_level_for_victim()
            elif character_choice == 'a':
                bullets = get_difficulty_level_for_assassin()
            ask_spin_cylinder()
            spin_story = get_spin_story(character_choice)
            ask_pull_trigger()
            survival_result = randomize_spin(bullets)
            message = get_result_message(character_choice, survival_result)
            slow_print(message)
            if not ask_play_again_or_quit():
                continue


main()
