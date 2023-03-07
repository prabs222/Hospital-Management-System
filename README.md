# Hospital-Management-System
A useful software for managing and operating day to day activities of a hospital in the most effective way.


## Setup Instructions

Clone the repo in your local system

```bash
  git clone https://github.com/prabs222/Hospital-Management-System.git
```
Install virtualenv

```bash
  py -m pip install --user virtualenv
```
Create a new Virtualenvironment

```bash
  py -m venv env
```
Activate the Virtualenvironment with

```bash
  .\env\Scripts\activate
```
Change directory to the folder

```bash
  cd folder-where-you-cloned-the-repo
```
Install all the requirements with

```bash
  pip3 install -r requirements.txt
```
Apply all the migrations with 

```bash
  python3 manage.py migrate
```
Run the developement server with 

```bash
  python3 manage.py runserver
```
You'll see output like this
```bash
  Performing system checks...

System check identified no issues (0 silenced).
July 04, 2022 - 15:50:53
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Tech Stack

**Server:** Django , Python

POSTMAN for API testing.

## Features

- APIs for the complete management of hospital services.
- Separate modules for receptionist, doctors and patients for the overall working of the hospital.


## Support++

This project needs your shiny star ⭐.   
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


##
([@prabs222](https://github.com/prabs222))
