# Hello Django

This is a code along project to learn Django.

---

## How Django works

- Django projects are organized into small components called apps.
    - You can think of an app as a reusable self-contained collection of code. That can be passed around from project to project in order to speed up development time.
- So if you need an authentication system for example that handles logging in
logging out password resets and so on.
Rather than build your own you could use a Django app. And simply install it into your project.
- Almost everything that we do in Django is going to revolve around these apps.

---

## Set up

- install Django: `pip3 install Django`
- create Django project: `django-admin startproject django_todo`
    - this will generate the project folder with a few ".py" files
    - `"__init__.py"` - tells our project that this is a directory we can import from
    - `"asgi.py"` - 
    - `"settings.py"` - contains globals settings for the entire Django project
        - whether we want to show debug information when errors happen
        - HTML templates location
        - which database we're going to connect to
    - `"urls.py"` -  contains the routing information that allows our users to type a specific URL into their address bar
        -  analogous to app.root in flask
    - `"wsgi.py"` - contains the code that allows our web server to communicate with our Python application
    - `__pycache__` directory - contains compiled python code
- `db.sqlite3` - this file will act as our database for the project
- run a Django project: `python3 manage.py runserver`

---

## Create an app

- create a Django app using `"manage.py"`: `python3 manage.py startapp todo`
    - this creates another folder called `"todo"` in the file explorer with a few ".py" files
    - `"migrations"` folder - 
    - `"__init__.py"` - 
    - `"admin.py"` - 
    - `"apps.py"` - 
    - `"models.py"` - 
    - `"tests.py"` - 
    - `"views.py"` - it's used to render some sort of an interface that allows our users to interact with the to-do items

### create a view

- in `"views.py"`, define a simple python function: `"say_hello()"`
- in `"urls.py"`, import `"say_hello()"` function
- define the url that's actually going to trigger the say hello function and return the http response to the browser: add `"path('hello/', say_hello, name='hello')"` to `"urlpatterns"`
- run server to see results: `python3 manage.py runserver`
- manually add `"/hello"` to the url in the address bar to see the results

---

*Disclaimer: this is a code along project from [Code Institute's](https://codeinstitute.net/) **Hello Django** module*