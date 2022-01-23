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
    - the built-in path function typically takes three arguments:
        - 1st arg is the url that the user is going to type in: `"hello/"`
        - 2nd arg is the view function that it's going to return: `"say_hello()"`
        - 3rd arg is a name parameter: `"hello"`
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
- The reason that we're creating this  secondary "todo" folder inside the "templates" directory is because when Django looks for templates inside of these apps it will always return the first one that it finds. 
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

## Create a model

A Django model is the built-in feature that Django uses to create tables, their fields, and various constraints. Django models simplify tasks and organize tables into models. Django models are used to store data in the database conveniently.

### Create a class

- in `"todo/models.py"` create a new class `"item()"` with 2 fields: "name", "done"
    - when Django sees that we've created a new item class it will automatically create an "items" table when we make and run the database migrations
    - by itself this class won't do anything we need to use "__class inheritance__" to give it some functionality
- use `"models.Model"` as argument in `"item()"` class to inherit the base model class to be able to start our own model with all of that base functionality
- define the attributes that our individual items will have: "name", "done"
    - we can skip the "Id" field since Django will create that for us automatically
    - `"null=False"` - prevents items from being created without a name programmatically
    - `"blank=False"` - makes the field required on forms
    - `"default=False"` - to make sure that to-do items are marked as not done by default

### Create the table in database

- make migrations "--dry-run" `"python3 manage.py makemigrations --dry-run"` - to see what it's going to do
- make migrations `"python3 manage.py makemigrations"` - to create model "item"
    - Django sees that we've added a new model to our app so it creates a new Python file in the migrations folder. That contains the code to create that database table based on our model. So this code will be converted to sequel by Django and executed on the database when we actually run the migrations
- use the `"python3 manage.py showmigrations"` command to see that we do in fact have an unapplied migration on our to-do app now
- run `"python3 manage.py migrate --plan"` to check not to do anything unintentional
- run `"python3 manage.py migrate"` to apply the migration on our to-do app

### Register the model

In order to be able to see our models in the admin panel on the server, we first need to expose them in `"admin.py"`
- import the "Item" model from ".models"
- use the `"admin.site.register()"` function to actually register our "Item" model

### Create a new item

- run the server: `"python3 manage.py runserver"`
- add __"/admin/"__ to the url
- click "items"
- click "add item" to add a new item
- add 2 items in our todo list

### Better visibility in the admin panel

The item object value in the admin is actually coming from the fact that the base Django model class was inherited when the item model was created.
By default all models that inherit the base model class will use its built-in string method to display their "class name" followed by the word "object" just so that there's a generic way to display them.

To change that we need to actually override that string method with our own.
And we can do that just by redefining it into our own class.

- create a new "`__str__()`" dunder method in `"todo/models.py"`
- run the server to view changes

---

## Rendering data

Now that we’ve saved our models data, we need to be able to render this data on our HTML templates for the users to be able to see.

### Adding an item key

- import the "Item" model from ".models" in `"todo/views.py"` to be able to use "item" model in the views
- modify `"get_todo_list()"` function to get a query set of all the items in the database in "items" variable
- create a variable "context" which is going to be a dictionary with all items in it
- add the "context" variable as a third argument to the render function to have access to it in the `"todo_list.html"` template

### Edit the `"todo_list.html"` template

- add a template variable `"{{ items }}"` to render the items key from the "context" dictionary
    - Anything that you return to the template in a dictionary can be rendered in the same way. That includes almost anything that you can use in Python. Meaning you can return strings, numbers, lists, other dictionaries, or even functions and classes.
- adjust items key to use a "for-loop" to create a "table" showing "item.name" and "item.done"
- update the "for-loop" add "if/else" statement to strike out an item if it's been done
- add an "empty" tag to handle what should happen if our database doesn't have any todo items in it

---

## Creating a new item

Now that we can render data from a Django database in a front-end HTML template, we're going to add the "Create" functionality, so that the users of our **todo_list** app to be able to interact with that data (to create their own todo items or mark them as complete).

Generally, with crud, you'll want different templates for different operations.

- create `"add_item.html"` template in `"templates/todo"` folder
- add a link to the new template in `"todo_list.html"`
- create a view in `"views.py"` to display the new template
- define the url for the new template in `"urls.py"`
- import the new `"add_item"` view to make it accessible to `"urls.py"`

- edit the `"add_item.html"` template to create a form for the user to enter a name for a todo item
- add a special template tag `"{% csrf_token %}"` to the form

- add "POST" functionality to the submit button by using an "if" statement in `"views.py"`
- run the server and add 2 items one done and on not to to check functionality

*__Important__*

- GET requests gets information from the server
- POST requests sends or posts information to the server
- to use POST request we need to add a special template tag `"{% csrf_token %}"` (cross-site request forgery token) to the form as a security measure
    - this token is a randomly generated unique value which will be added to the form as a hidden input field when the form is submitted. 
    - and works to guarantee that the data we're posting is actually coming from our todo list app and not from another website.

---

## Modifying Data

### Using forms

Creating forms manually leaves our application open to errors if we don't validate them properly. To alleviate this issue. In Django it's possible to create forms directly from the model itself. And allow Django to handle all the form validation.

- create a new file in the `"todo"` app directory called `"forms.py"`
- import forms from django
- import Item model from .models
- create a new class ItemForm() that inherits all the functionality of forms.ModelForm
- create an inner class called meta to tell the form which model it's going to be associated with
- in `"views.py"` import "ItemForm" from ".forms" 
- create an instance of it in "add_item" view
- create a "context" which contains the empty form
- return the "context" to the template
- in `"add_item"` template replace the form content with `{{ form }}` template variable
- in `"add_item"` view replace the name and done fields, and Item.objects.create
- in `"add_item"` template adjust the styling of the form to vertical styling: `"{{ form.as_p }}"`

### Editing an Item

Now that our todo app has the ability to create items we'll give it the ability to edit existing items.

- in `"todo_list"` template add an edit button to each table row
- in `"views.py"` create a new view called `"edit_item"`
- create a new template called `"edit_item.html"`
- in `"urls.py"` create a new path which will point to `"edit/<item_id>"`
- in `"edit_item"` view get a copy of the "item" from the database by using a built in django shortcut called `"get_object_or_404()"`
- write a "POST" handler in the `"edit_item"` view

---

*Disclaimer: this is a code along project from [Code Institute's](https://codeinstitute.net/) **Hello Django** module*