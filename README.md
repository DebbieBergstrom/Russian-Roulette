# **Russian Roulette Game**

Welcome to our cheerful yet suspenseful Python game, a playful spin on Russian Roulette. Enjoy this text-based adventure, enhanced with colors and ASCII art. As you engage with this thrilling narrative, every round becomes a delightful dance with fate. Join the fun and let's see if you can outwit destiny!

![amiresponsive](/docs/images/amiresponsive_pp3.png)

*Please have a look at the deployed app ![here.](https://russian-roulette-game-f11e249e6274.herokuapp.com/)*

&nbsp;

![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=flat)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=flat)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=flat)

---

## **CONTENT**
- [UX](#ux)
- [User Stories](#user-stories)
- [How to use Russian Roulette Game](#how-to-use-russian-roulette-game)
- [Program Flow](#program-flow)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

&nbsp;

---

## **UX**
### **Site Purpose**

To engage users in a thrilling game of virtual Russian Roulette. Users can play, testing their luck and surviving the suspenseful rounds.

### **Site Goal**

To offer a simple, entertaining and suspenseful game experience through a terminal-based text game.

### **Audience**

Individuals who enjoy text-based games, probability, suspense, and testing their luck.

### **Communication**

The game communicates its intent through print statements, prompting the user to choose options and make their game decisions. Different outcomes are highlighted in different colours to increase user engagement and improve readability.

### **Current User Goals**

To keep the user engaged with the game by offering a captivating and suspenseful experience. The ability to restart the game provides the user with opportunities for endless fun and varying outcomes.

### **New User Goals**

To learn the mechanics of the game, enjoy the suspense, and challenge their luck in the game.

### **Future Goals**

To expand the game by implementing more fun features, please see the list of Future features further down. 


## **User Stories**
#### **First time users**
1. _As a first-time user, I want to 
2. _As a first-time user, I want to 
3. _As a first-time user, I want to 
4. _As a first-time user, I want to 
5. _As a first-time user, I want to 
6. _As a first-time user, 

#### **Returning users**
7. _As a returning user, I want to
8. _As a returning user, I want to
10. _As a returning user, I want to
11. _As a returning user, I want to 

&nbsp;

---
## **How to use Russian Roulette Game**
Press the button to start the game and test your fate. In this game, you first choose your role as either the assassin or the victim. Then, select the level of difficulty. Based on your choice, a revolver is loaded with 1, 2, or 3 bullets, and the cylinder is spun to randomize the position of the bullets. If you're the victim, you'll be forced to pull the trigger. Your fate hinges on the outcome: if the gun fires, you lose and the assassin prevails. If it doesn't, you survive and the assassin walks away. Navigate through the game by pressing the prompted keys followed by the 'Enter' key. Get ready for a fun game of luck and chance!


&nbsp;

---

## Design

The design of the game incorporates various elements to enhance the user experience and game atmosphere. Inside the terminal, colorful ASCII art has been utilized to provide visual feedback and further immerse the user in the gameplay.

In addition to the terminal, the design also extends to the surrounding environment with a background featuring a close-up of a revolver with an open cylinder. With o monochromatic palette of black, grey, and white to represent the serious and suspenseful theme of the game, the image helps to set the mood and theme of the game, in contrast to the previous plain white background.

Moreover, a header has been incorporated stating "You just entered a deadly game of Russian Roulette", serving as an intriguing introduction that instantly catches the user's attention.

Complementary colors like red and yellow are used strategically in the heading and the button that says "Test your fate".

![Color Scheme](/docs/images/color_scheme_pp3.png)

---

## **Program flow**

FLowchart made in LucidChart displays all of the steps of the game from beginning to end. 
![flowchart](/docs/images/lucid_chart_PP3_russian_roulette.png)


&nbsp;

---
## **Technologies used**
### **Language**
- <b>Python 3</b>: Primary programming language for the project.
- <b>HTML5</b>: basic structure from Code Institute Template. Code was added to change styling for this app.
- <b>CSS</b>: basic structure from Code Institute Template. Code was added for styling of background, heading and button.
- <b>Javascript:</b> from Code Institute Template. 


### **Programs used**
- [LucidChart](https://lucidchart/) to visually map out the structure and flowchart of the app.
- [Gitpd](https://gitpod.io/) cloud-based IDE used for version control and writing code
- [Git](https://git-scm.com/) version control system used for managing and tracking changes to the project's codebase
- [Github](https://github.com/)  web-based hosting service used for version control and storing the project's code after being pushed from Gitpod
- [Heroku](https://www.heroku.com/home) cloud platform used for deploying and hosting the project's web application
- [Pseudoeditor](https://pseudoeditor.com/app/) For making a structured plan of pseudocode before actual Python coding.


&nbsp;

---
## **Features**
### **Existing features**

The **Russian Roulette Game** application currently offers the following features:

<details><summary>Landing page - Welcoming the user to the game: </summary>
<img src="/docs/images/landing_page.png"></details>

<details><summary>Introduction to the game - followed by choice to be the victim or the assassin or see rules: </summary>
<img src="/docs/images/intro_choose_character.png"></details>

<details><summary>Story based on character choice displays - The storyline will from now on be different for 'victim' and 'assassin': </summary>
<img src="/docs/images/story_for_character.png"></details>

<details><summary>Game Rules -Users can choose to see the game rules, helping newcomers to quickly understand the gameplay mechanics: </summary>
<img src="/docs/images/see_rules.png"></details>

<details><summary>Difficulty level - allows users to select a difficulty level (easy, medium, hard), affecting the number of bullets loaded into the revolver: </summary>
<img src="/docs/images/level_for_character.png"></details>

<details><summary>Interactive Gameplay - engages users with prompts and feedback based on their choices.</summary>
<img src="/docs/images/guns_loaded.png">
<img src="/docs/images/spinning.png">
<img src="/docs/images/cylinder_spun.png">
<img src="/docs/images/pull_trigger_invalid.png">
</details>

<details><summary>ASCII Art Visuals - The game uses colored ASCII art to enhance the storytelling and to display the results of each round: </summary>
<img src="/docs/images/boom.png"></details>

<details><summary>Random Outcomes displays different Game Result Messages - Every game session is unique due to the randomized position of bullets in the revolver. Upon game conclusion, users are presented with a fun ASCII art message indicating whether they have survived or not:</summary>
<img src="/docs/images/survived_for_character.png">
<img src="/docs/images/death_for_character.png">
</details>

<details><summary>Replayability - The game allows for immediate replay upon conclusion, offering users another chance to test their luck. Otherwise a goodbye message displays telling the player the game ends:</summary>
<img src="/docs/images/game_ends.png">
</details>

&nbsp;

### **Future Ideas**
The development of **Russian Roulette Game** aims to provide more immersive and personalized experiences to users in the future. Here are some of the potential enhancements and features that may be implemented:

- **Expanded Story Options:** Broaden the narrative by introducing more storylines or story options for users to engage with.

- **Character Personalization:** Offer the option for users to name their victim character, providing a more personalized experience.

- **Contractor Selection:** Allow the assassin to choose from a list of evil contractors they've been hired from, adding a new layer of depth to the game's storyline.

- **Dual Victim Mode:** Introduce a mode where a second victim can play against the assassin, adding another layer of competition and suspense to the game.

- **Enhanced Story Interactions:** Further develop the game's interactive elements, enabling users to make choices that have impacts on the storyline's direction and outcomes.

- **Game Progress Saving:** Implement a feature to store game scores or outcomes, allowing users to track their performance.

- **Sound Effects:** To enhance the immersive experience, sound effects could be added to match different events or outcomes within the game.

&nbsp;

---
## **Validation**

- All string inputs are made case-insensitive with the `.lower()` function. This prevents users from encountering errors due to letter casing.

- The `validate_input` function is used to maintain input validity at all stages. This function asks for user input until a valid input is provided, ensuring that the program doesn't break due to unexpected inputs. Valid inputs are defined as per the game requirements at each step.

- In case of invalid inputs, an error message is displayed to the user. This message guides the user about the correct format or type of expected input, leading to a smoother user experience.

- The `slow_print` and `slow_input` functions ensure a comfortable pace for users to read the prompts and game descriptions and provide their inputs accordingly. This prevents any rush or confusion while playing the game.


&nbsp;

---
## **Testing**

### **Testing User Stories**

**First Time Visitors**
| User Story | How this was achieved | Screenshot |
|------------|-----------------------|------------|
| As a first-time visitor, I want to | The application displays a  | <details><summary>Screenshot of result:</summary><img src="/docs/images/">
</details> |

&nbsp;

**Returning Visitors**
| User Story | How this was achieved | Screenshot |
|------------|-----------------------|------------|
| As a returning visitor, I want to  | Returning visitors can | <details><summary>Screenshot of result:</summary><img src="/docs/images/"> |


&nbsp;

### Automated Testing
The * [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#) validator was used to validate all Python modules in this project.

* The `run.py` file was validated without any errors:

    <details><summary>See the validation results</summary>
    <img src="/docs/testing/py_linter_runpy.png">
    </details>

* The `all_functions.py` file was validated without any errors except for some necessary white spaces needed within the 'spinning' ASCII art string:

    <details><summary>See the validation results</summary>
    <img src="/docs/testing/py_linter_all_functions.png">
    </details>

* The `ascii.py` file was validated with errors only relating to necessary white spaces and indentation needed within all the ASCII art strings:

    <details><summary>See the validation results</summary>
    <img src="/docs/testing/py_linter_ascii.png">
    </details>

&nbsp;

### Manual Testing
Family and friends tested my game application on their devices and no issues were reported.

**TEST** | **ACTION** | **EXPECTATION** | **RESULT**
----------|----------|----------|----------|
get_character_choice() | Input (v) for 'victim', (a) for 'assassin', or (r) for 'rules' | Game character is selected or rules are displayed | All three works as expected |
get_character_choice() | Input invalid choice (anything other than (v), (a), or (r)) | Error message displays: "Only the provided options are valid. Choose one of them." | Works as expected |
get_difficulty_level() | Input difficulty level ('low'(1), 'medium'(2), 'high'(3)) | Difficulty level is set according to input | All three works as expected |
get_difficulty_level() | Input invalid difficulty level (anything other than (1), (2), (3)) | Error message displays: "Only the provided options are valid. Choose one of them." | Works as expected |
ask_spin_cylinder() | Input (s) to 'spin' | Function indicating cylinder is spinning is executed | Works as expected |
ask_spin_cylinder() | Input anything other than (s) to 'spin' | Error message displays: "Only (s) is valid. There's no turning back..." | Works as expected |
ask_pull_trigger() | Input 'enter' to Pull the trigger | Function indicating the trigger is pulled is executed | Works as expected |
ask_pull_trigger() | Input anything other than 'pull' | Error message displays: "Don't extend the suffering. Press only (enter)" | Works as expected |
ask_play_now_or_quit() | Input 'Yes'(Y) to question if player want to play now | Game goes back to where it started if 'Y' is pressed | Works as expected |
ask_play_now_or_quit() | Input 'No'(N) to question if player want to play now | Game ends and displays message: "Welcome back! Game ends..." | Works as expected |
ask_play_now_or_quit() | Input anything other than 'Yes'(Y) or 'No'(N) | Error message displays: "Only the provided options are valid. Choose one of them." | Works as expected |
ask_play_again_or_quit() | Input 'Yes'(Y) to question if player want to play again | Game starts/continues or exits based on the input | Works as expected |
ask_play_again_or_quit() | Input 'No'(N)  to question if player want to play again | Game ends and displays message: "Nuff action for today, huh. See you next time! Game ends..." | Works as expected |
ask_play_again_or_quit() | Input anything other than 'Y' or 'N' | Error message displays: "Only the provided options are valid. Choose one of them." | Works as expected |


&nbsp;

---
## **Bugs**

| **Bug** | **Fix** |
| ----------- | ----------- |
| 1. The first line of the multiline string is not aligned with the rest that gets indented.| Concatenate string by string wrapped in "" with a "+" at the end and avery new string beginning with "n\"|
| 2. Validation and error message didn't work on the play_now/play_again inputs.| Fixed by using the correct validate_input function|
| 3. Validation error message kept being displayed even if prompted key 'enter' was pressed.| Fixed by setting en empty string [''] instead of [enter].|                                                                                                                                                                   

&nbsp;
### **Unfixed Bugs**
| **Bug** | **Possible solution** |
| ----------- | ----------- |
| 1. When player has chosen difficulty level and the viewport of the screen in the terminal gets 'cleared' (previously content isn't visible any longer in case player dosn't scroll up), if player scroll up you see that the previously displayed ascii 'syringe' is cut in half | I deleted all the "os.system('clear')" out of the code, but when the game runs it gets all run from top to bottom without any effect of cleared viewport window and it does not look good and takes away some of the suspense that is built up through choices made through the story. Therefore this is left unfixed since it's not meant to scroll up anyway and the 'clear' function adds more to the game than if its not executed. |  


&nbsp;

---
## **Deployment**
To deploy this project, these steps was followed:

1. Fork and clone this repository to your local machine.
2. Create a new Heroku app.
3. In the Heroku dashboard, navigate to the app's settings and set the buildpacks to Python and NodeJS in that order.
4. Connect your Heroku app to the repository by linking it to your forked copy of the repository.
5. Click on the "Deploy" button in the Heroku dashboard.

After following these steps, the app was successfully deployed to Heroku. 

&nbsp;

---
## **Credits**

### Here's a collection of sites that were helpful in creating this website:

- [WC3Shools](https://www.w3schools.com/python/ref_func_input.asp) Explaining input function
- [WC3Shools](https://www.w3schools.com/python/python_while_loops.asp) Explaining while loops
- [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/) Explaining clear screen and sleep import
- [GeeksforGeeks](https://replit.com/talk/learn/The-Slow-Print/44741) Explaining delayed printing

- [Youtube](https://www.youtube.com/watch?v=jSv0coMSQgg) First tutorial russian roulette game
- [Youtube](https://www.youtube.com/watch?v=lJivq450kqQ) Second tutorial russian roulette game
- [Youtube](https://www.youtube.com/watch?v=lqAQN0T_Ues&t=580s) Third tutorial russian roulette game

- [ASCII Art](https://https://www.asciiart.eu/weapons/guns) For pre-made ASCII weapon art
- [ASCII Textcool](https://textkool.com/en) ASCII text generator
- [Wallpaperflare](https://www.wallpaperflare.com/cartridge-revolver-russian-roulette-wallpaper-goipr/download) For free backround image

- [PsuedoEditor](https://pseudoeditor.com/app/) To create pseudocode to help structure the app
- [Termocolor](https://pypi.org/project/termcolor/) To create colored text output

- [ChatGPT](https://openai.com/) To create some of the story content

- Code Institute, Python learning material.

---

###  **Acknowledgments**

I'd like to give recognition to the ones who have supported me in finishing this project:

* [Lauren_Nicole](https://github.com/CluelessBiker), my Code Institute Mentor. I cannot thank her enough for her invaluable guidance and assistance.

* [Sandra B](https://github.com/SandraBergstrom) and [Kim B](https://github.com/KimBergstroem), my dear siblings who are with me on this coding journey and who are both great critics and support pillars.

* Code Institute and their helpfull staff, especially within our great Slack community. 

[Back to top](#)
