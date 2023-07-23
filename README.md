# **Russian Roulette Game**

Welcome to 

![amiresponsive](image url)

*Please have a look at the deployed website ![here.](site url)*

&nbsp;

![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=flat)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=flat)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=flat)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=flat)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=flat)

---

## **CONTENT**

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
...........


&nbsp;

---
## **Program flow**


![flowchart](/docs/screenshots/lucid_chart_PP3_russian_roulette.png)

&nbsp;

---
## **Data model**
The app did not use a data model at this stage of development.


&nbsp;

---
## **Technologies used**
### **Language**
- <b>Python 3</b>: primary programming language for the project


### **Programs used**
- [LucidChart](https://lucidchart/) to visually map out the structure and flowchart of the app.
- [Gitpd](https://gitpod.io/) cloud-based IDE used for version control and writing code
- [Git](https://git-scm.com/) version control system used for managing and tracking changes to the project's codebase
- [Github](https://github.com/)  web-based hosting service used for version control and storing the project's code after being pushed from Gitpod
- [Heroku](https://www.heroku.com/home) cloud platform used for deploying and hosting the project's web application
- [Pseudoeditor](https://pseudoeditor.com/app/) For making a structured plan of pseudocode before actual coding.


&nbsp;

---
## **Features**
### **Existing features**
The <b>Russian Roulette Game</b> application currently offers the following features:

- <b>Character choice:</b> Users can choose to be the victim or the assassin.

### **Future ideas**
Expanded features Options: Provide more storylines or story options to allow users to select and engage with different narrative paths.

- <b>Personalization:</b> Offer the option for users to name their player character.
- <b>Enhanced Story Interactions:</b> Develop interactive elements within the storylines, allowing users to make choices that have more significant impacts on the narrative.
- <b>Improved Validation and Error Handling:</b> Refine the validation and error handling mechanisms to provide more informative and user-friendly error messages in case of incorrect inputs or invalid data.
- <b>Save data:</b> for example to store scores

&nbsp;

---
## **Validation**
All string validations have the <b>`.capitalize()`</b> or <b>`.upper()`</b> function to prevent any big or small letter errors.

### **All (Y)es or (N)o question validation:**
- If used with an IF statement as below code: &nbsp;

    `if` "N" `not in` "variable" `and` "Y" `not in` "variable":
    `print('Please press either "Y" for YES or "N" for NO')`

&nbsp;

---
## **Testing**

### **Testing User Stories**

**First Time Visitors**
| User Story | How this was achieved | Screenshot |
|------------|-----------------------|------------|
| As a first-time visitor, I want to | The application displays a  | <details><summary>Screenshot of result:</summary>![Result](docs/testing)</details> |

&nbsp;

**Returning Visitors**
| User Story | How this was achieved | Screenshot |
|------------|-----------------------|------------|
| As a returning visitor, I want to  | Returning visitors can | <details><summary>Screenshot of result:</summary>![Result](docs/testing/)</details> |


&nbsp;

### Automated Testing
The <b>PEP8</b> validator was used to validate all Python modules in this project. No errors were found besides warnings on some lines that are too long, which can't be undone or shortened.

  * [PEP8 - run.py](https://pep8ci.herokuapp.com/#)
    ![run.py file](docs/testing/)

* [PEP8 - converter.py](https://pep8ci.herokuapp.com/#)
    ![converter.py file](docs/testing)

* [PEP8 - currency_data.py](https://pep8ci.herokuapp.com/#)
    ![currency_data file](docs/testing/)

* [PEP8 - text_colors.py](https://pep8ci.herokuapp.com/#)
    ![text_colors.py file](docs/testing/)


&nbsp;

### Manuell Testing
Family and friends tested my game on their devices no issues were reported.

**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
Validation of integer inputs for "Y" and "N" questions	| test input of both lower- and uppercase	| both should work as inputs | Works as expected


&nbsp;

---
## **Bugs**

| **Bug** | **Fix** |
| ----------- | ----------- |
| 1. The first line of the multiline string is not aligned with the rest that gets indented.| TO BE FIXED|
| 2. Validation and error message didn't work on the play_now/play_again inputs.| Fixed by using the correct validate_input function|
| 3. Validation error message kept being displayed even if prompted key 'enter' was pressed.| Fixed by setting en empty string [''] instead of [enter].|                                                                                                                                                                   

&nbsp;
### **Unfixed Bugs**
| **Bug** | **Possible solution** |
| ----------- | ----------- |
| 1. Bug to be listed| Solutions to be fixed ||   


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

- [WC3Shools](https://www.w3schools.com/python/ref_func_input.asp) explaining input function
- [WC3Shools](https://www.w3schools.com/python/python_while_loops.asp) explaining while loops
- [GeeksforGeeks](https://www.geeksforgeeks.org/clear-screen-python/) explaining clear screen and sleep import
- [GeeksforGeeks](https://replit.com/talk/learn/The-Slow-Print/44741) explaining delayed printing

- [Youtube](https://www.youtube.com/watch?v=jSv0coMSQgg) first tutorial russian roulette game
- [Youtube](https://www.youtube.com/watch?v=lJivq450kqQ) second tutorial russian roulette game
- [Youtube](https://www.youtube.com/watch?v=lqAQN0T_Ues&t=580s) third tutorial russian roulette game

- [ASCII Art](https://https://www.asciiart.eu/weapons/guns) for pre-made ASCII weapon art
- [ASCII Textcool](https://textkool.com/en) ASCII text generator


- [ChatGPT](https://openai.com/) To create some of the story content

---

###  **Acknowledgments**

I'd like to give recognition to the individuals who supported me in finishing this project:

* Thanks to... tbc

* [MENTOR NAME](https://github.com/??????????), my Code Institute Mentor.....tbc

<p align="right">(<a href="#readme-top">back to top</a>)</p>
