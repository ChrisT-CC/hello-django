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

## Create a view

- in `"views.py"`, define a simple python function: `"say_hello()"`
- in `"urls.py"`, import `"say_hello()"` function
- define the url that's actually going to trigger the say hello function and return the http response to the browser: add `"path('hello/', say_hello, name='hello')"` to `"urlpatterns"`
- run server to see results: `python3 manage.py runserver`
- manually add `"/hello"` to the url in the address bar to see the results

---

## Create a template

- in the `"todo"` folder, create a new folder called `"templates"`
- in the `"templates"` folder, create a new folder called `"todo"`
- in the new `"todo"` folder, create a new file called `"todo_list.html"`
- `"todo_list.html"` will act as first template
- generate html boilerplate for `"todo_list.html"` including a h1 tag, "Things I need to do:"
- update `"say_hello()"` function with `"render"` function in `"views.py"`
    - the `"render"` function takes an HTTP request and a template name as it's two arguments and it returns an HTTP response which renders that template
- rename `"say_hello()"` with `"get_todo_list()"`
- in `"urls.py"`, replace the `"say_hello"` path and update imports
- add our `"todo"` app in `"settings.py"` file in `"INSTALLED_APPS"`

*__Important__*
- The reason that we're creating this  secondary todo folder inside the templates directory is because when Django looks for templates inside of these apps it will always return the first one that it finds. 
- So by separating it into a folder that matches its app name, we can ensure that we're getting the right template even if there's another template of the same name in a different app.

---

## Migrations and Admin

Migrations are Django's way of converting Python code into database operations i.e. they allow us to store our data in the database on the backend.

### Step 1: Make migrations
- `"python3 manage.py makemigrations --dry-run"` - runs a test migration run
- `"python3 manage.py showmigrations"`- shows some built-in Django apps like authentication and the Django admin and a couple of others that already have some migrations that need to be applied
    -  applying these migrations we'll set up the database and allow us to create an admin user that we can use to manage it
- `"python3 manage.py migrate --plan"` - we use the plan flag in order to see what it's going to do
    - it shows us the initial migrations that are going to take care of some basic requirements like setting up the users groups and permissions tables. And altering the fields on some of those tables.
- `"python3 manage.py migrate"` - takes care of theinitial setup

### Step 2: Create Superuser

A django superuser is the most powerful user with permissions to create, read, update and delete data in the Django admin, which includes model records and other users. A superuser is also able to login to the admin site.

One of the most powerful parts of Django is the *__automatic admin interface__*. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.
- `"python3 manage.py createsuperuser"` - creates a Super User
- create username and password
- `"python3 manage.py runserver"` - run the server
- add __"/admin/"__ to the url
- __"login"__ to see the authentication and authorization app that's been created and the two tables users and group that have been created inside that app

---

*Disclaimer: this is a code along project from [Code Institute's](https://codeinstitute.net/) **Hello Django** module*