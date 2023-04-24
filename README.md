# Crave and Feast

Crave and Feast is a website application designed to help busy people create culturally diverse, nutrient dense meals. This web app was created to reduce food waste by encouraging users to use food that is already at home. 

Crave and Feast uses React frontend and Python and Flask on the backend while using Google Firebase Cloud Firestore for its databse. It also aggregates recipes by using an recipe search API. Users are able to register or sign into account and search for recipes. They are also able to save or remove saved recipes from their profile page

## Demo
***
[{Crave and Feast Demo Link}](https://www.loom.com/share/e364226cb1d64206ba988a5233a4691a)

## Features
***
* Can register and sign-in to access account
* Can find recipes based on ingredients typed into dashboard
* Can create a profile page to customize experience
* Can add favorite recipes to profile page by hearting
* Can remove favorite recipes to profile page by hearting within profile page
* Accessible navigation using keyboard

## API
***

Crave and Feast uses Edamam Recipe Search API. An API call was completed to 
* Get recipes based on ingredients searched
* Get recipes that populate homepage
* Read saved recipes on user's profile
* Delete favorite recipes by unfavoriting recipe on profile page

## Cloud Firestore
***

Crave and Feast used firestore to manage user data
* User registration
* Authenticate user login information
* Add favorite recipes
* Delete favorite recipes


## Installation
***
#### Backend
* Fork this repository. 
* This will make a copy of the source code onto your github
* Clone your forked repository by using the command 
```git clone```
* Install python by using this command
  `python3 -m venv venv`
* Create a virtual environment
  `source venv/bin/activate`
* Install requirements
  `pip install -r requirements.txt`
* Install Flask
  `python -m pip install flask`
* Run project on your local machine with this command
  `FLASK_ENV=development flask run`

#### Google Firebase
* Sign up for Firebase
* Create Project
* Create Firestore Database


