<h1 align="center"> Wiki Translate </h1>

<div align="center" text-align="center">
  
![version](https://img.shields.io/badge/version-1.0.0-blue.svg) ![license](https://img.shields.io/badge/license-MIT-brightgreen)
  
</div>
  
## About
Wiki Translate is a Django Web App deployed at (https://wikitranslateavi.herokuapp.com/). It basically extracts summary of a wikipedia article and allows user to input and save sentence wise translation. Languages accepted are - Hindi, Punjabi, Bengali, Tamil, Telugu.

## Table of Contents
- [Features implemented :boom:](#features-implemented)
- [How to use](#how-to-use)
- [Installation 🐣](#installation)
- [Starting the app](#starting-the-app)

## Features Implemented
- Storing article title and target language.
- Extraction of article summary from article title.
- Splitting summary into sentences using nltk tokenizer.
- Storing sentence wise translation to target language entered by user.
- Transliteration, that is, support for typing in the target language.
- Heroku Deployment

## How to use
1. Go to the website https://wikitranslateavi.herokuapp.com/
2. Enter any WikiPedia article name, select target language from the dropdown and click Translate.
3. Summary of the article will be shown on the same page.
4. Scroll down to Available Projects and select your project from the list.
5. A page displaying sentence wise summary and text boxes will come up.
6. Enter your translation for the sentences. Typing support for target language is available.
7. When done, click submit button at the bottom of the page.
8. Your translation is saved. The text boxes will be auto filled whenever someone accesses your project.

## Installation

Follow these steps to install this project directory:

```
# clone the repo
$ git clone https://github.com/Aviral09/wikitranslate.git

# install dependencies
$ pip install requirements.txt

# go into app's directory:
$ cd wikitranslate
```

## Starting the app

Follow these steps to run the app on your local machine:

```
# go into app's directory:
$ cd wikitranslate

# Make database migrations
$ python manage.py makemigrations

# Apply database migrations
$ python manage.py migrate
  
# launch the app
$ python manage.py runserver

```
