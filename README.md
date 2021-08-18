![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Calorie-calculator

This project Calorie-calculator is an online calculator to help woman work out their BMR, CAlories needed to loose weight and calories needed to gain weight.



A deployed version of my website can be found [here.] ()

## navigation

* [UX](#ux)
  + [UX-stories](#ux-stories)
* [Strategy](#strategy)
  + [User-needs](#user-needs)
  + [Business-vision](#business-vision)
* [Scope](#scope)
* [Structure](#structure)
* [Features](#features)
* [Technologies](#technologies)
* [Testing](#testing)
  + [Testing-plan](#testing-plan)
  + [Implementation](#implementation)
  + [Results](#results)
* [Bugs](#bugs)
* [Deployment](#deployment)
* [Credits](#credits)
* [Content](#content)
* [Acknowledgements](#acknowledgements)

## UX

User stories
## First time visitor goals

* As a first time visitor, my aim is for the user to find it easy to submit their stats.
* As a first time visitor, my aim is for user to feel confident using the calculator.

## Returning visitor goals:

* As a returning visitor, my aim is for the user to re-submit new data when after a few weeks of following the calculators advice.
* As a returning visitor, I want my calculator to fill the user with hope and confidence to achieve thier goal.


The end goal of the project is to help the user achieve thier goal, whether that is to loose weight, gain weight or just maintain their current weight.

### UX stories

* As a user I want a find out the inforamation using the data I gave.
* As a user I want to be able to return and re-submit new data as I nearer my goal.


## Strategy

### User Needs

As a user the site has to be easy to use, straight forward and simple questions.

### Business vision

The purpose of this project is to give users a hope and help to achieve their goals.

## Scope

I want my users to feel they have a plan to move forward with thier goal using the online calculator. 

## Structure

This project is a simple online platform, which uploads the data to googlesheets where teh calculations are work out.


## Features

This section contains some of the features this project contains:
* My calculator is a one page display
* Asking 3 simple questions, Weight in KG, Height in Cm and Age.
* the platform will upload the data into the relevant rows and columns in google sheets.
* It will then calculate the BMR, Caloie Deficit and Calorie Surplus.
* The user will then take the relevant info to suit thier goal.


## Technologies

This project was build using the following technologies:

### Languages
* python 3

### Libraries and online resources:
* http://pep8online.com/checkresult to check my code for errors.
* README template from code institute fellow student [README.md template](https://github.com/ThijsTerporten/Climbing-Traveller/blob/master/README.md).
* GSPREAD
* Code along Love Sandwhiches to get me going.
* Formula to work out BMR for a woman (https://www.garnethealth.org/news/basal-metabolic-rate-calculator)
* Stack Overflow to help and advice when my code wasn't working
* Slack comminity for advice when my code wasn't workin 

### Testing

## Testing Plan

I have tested my code in (http://pep8online.com/checkresult).

### Testing User Stories from User Experience (UX) Section

## First Time Visitor Goals

As a First Time Visitor, I want to easily understand the instructions.

* Upon entering the calculator, users are automatically greeted with a welcome message.
* Then the a short paragraph stating the user is to use numbers only for thier answers not words as the calculator won't work.
* Then the first question enter your weight in kg
* Next question enter your height in cm
* Finally enter your age.

* The calculator has been designed to be fluid and easily explained, easy to use.

## Returning Visitor Goals

As a Returning Visitor, I want the visitor to remeber the questions and re-submit thier new stats.


## Frequent User Goals

As a Frequent User, I want to upload my new stats according to my progress so I can set a new goal.

* The user would already be comfortable with the calculator layout and can easily access teh answers.
* As a Frequent User, I want them to check to see if there are any new infomation, advice or improvments.

### Further Testing

* I have tested my code in (http://pep8online.com/checkresult).

### Implementation

As this is the third project that I created on my own I had very little experience debugging on my own. Testing was mainly done using (http://pep8online.com/checkresult). in google chrome. 


### Results

Once I had a general idea on how to run testing I followed all steps for each of my pages which gave me the following results for the python code:


Code	Line	Column	Text
W291	32	69	trailing whitespace
E501	123	80	line too long (88 > 79 characters)
E501	135	80	line too long (84 > 79 characters)
E501	147	80	line too long (88 > 79 characters)
E501	159	80	line too long (84 > 79 characters)



* Python check: [run.py](images/PEP_Results.JPG)



### Bugs

#### Python

I found writting my own Python quite complex and time consuming, after more research on Slack, Stack Overflow and youTube, (youtube found in credits section) I overcome most bugs, for loops. 

The only things that remain are the lines of code are too long. I'm not sure how to rectify this, but will do more research for future projects.


## Deployment

This project is deployed using gitpod in combination with github pages.
I used gitpod to write all code and seeing it is linked with github it was easy to use the terminal to commit.

### Heroku



## Making a Local Clone

1. Log in to GitHub and locate the GitHub Repository
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

7. Press Enter. Your local clone will be created.

$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.


## Credits 

* Love Sandwiches code along for inspiration of what project to use.
* Website to help with Formula to work out BMR for a woman (https://www.garnethealth.org/news/basal-metabolic-rate-calculator)
* README template from code institute fellow student [README.md template](https://github.com/ThijsTerporten/Climbing-Traveller/blob/master/README.md).
* My own personal goal with fitness and nutrition.
* Online resources to fnd out errors Stack Overflow, YouTube, W3School.
* Slack community.
* Tutor support. 

## Content

All content in this project are taken from my own goal for fitness and nutrition and Website to help with Formula to work out BMR for a woman (https://www.garnethealth.org/news/basal-metabolic-rate-calculator)


## Acknowledgements 

I would like to acknowledge my felow students on Slack community, Sean at Tutor support. He reassured me when I was doubtful of myself and my skills, about things he saw I was struggling with. And myself, Python ws very complex and I found it very hard at times my Impostor Syndrome at it worse, but I research, put a lot of hours in and finally my code work.

**This project was created for educational purposes only, credit for all images goes to their owners**

**Created by Mel Watts**
