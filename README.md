<h1 align="center"> Ecommerce Rest API </h1> <br>

## Table of Contents


- [Features](#features)
- [Project Demo](#project-demo)
- [Running this project](#running-this-project)


## Features

A few of the things you can do with this app:

* Admin can create/update/delete Product Category
* Admin can create/update/delete Product Detail
* Authenticated Users can make POST requests to Product Category & Product Detail
* Unauthenticated Users can only make GET requests to Product Category & Product Detail
* Users can SignUp to be authorized
* Authorized Users can make Payment & Order Products

## Project Demo

### Live Demo

Live Project url: [ecommerceapi4.pythonanywhere.com](https://ecommerceapi4.pythonanywhere.com/)

### API Documentation Page

<p>
  <img src = "https://user-images.githubusercontent.com/83788662/155869938-b1f6ccc9-d45a-44bc-b512-7572c4f58462.jpg" width=700>
</p>



## Running this project


To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with
```
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
```
virtualenv env
```
That will create a new folder ```env``` in your project directory. Next activate it with this command on mac/linux:
```
source env/bin/active
```
Then install the project dependencies with
```
pip install -r requirements.txt
```
Now you can run the project with this command
```
python manage.py runserver 
```
