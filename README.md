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

One of the most powerful parts of Django is the *__automatic admin interface__*. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin???s recommended use is limited to an organization???s internal management tool. It???s not intended for building your entire front end around.
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

Now that we???ve saved our models data, we need to be able to render this data on our HTML templates for the users to be able to see.

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

## Modifying Data using forms

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

---

## Editing an Item

Now that our todo app has the ability to create items we'll give it the ability to edit existing items.

- in `"todo_list"` template add an edit button to each table row
- in `"views.py"` create a new view called `"edit_item"`
- create a new template called `"edit_item.html"`
- in `"urls.py"` create a new path which will point to `"edit/<item_id>"`
- in `"edit_item"` view get a copy of the "item" from the database by using a built in django shortcut called `"get_object_or_404()"`
- write a "POST" handler in the `"edit_item"` view

---

## Toggling an Item

- add a "toggle" link in `"todo_list"` template
- add a new path "toggle" in `"urls.py"` file and modify import views
- create a new view `"toggle_item"`
- run server and check functionality

---

## Deleting an Item

- add a "delete" link in `"delete_list"` template
- add a new path "delete" in `"urls.py"` file and modify import views
- create a new view `"delete_item"`
- run server and check functionality

---

## Testing forms in Django

Django has a testing framework available that can be used to create automated tests. 

- rename the "test" file to `"test_forms.py"`
- import "TestCase" form "django.test" and "ItemForm" from ".forms"
- create a class `TestItemForm(TestCase):` that inherits "Testcase" and contain all the tests for this form
1. test to check that item name is required: `test_item_name_is_required`
    - create a form instance with an empty name field stored in "form" variable
    - check that this field is not valid
    - check that there is a "name" key in the dictionary of form errors
    - check whether the error message on the name key is "This field is required."
1. test to ensure the done field is not required: `test_done_field_is_not_required`
    - create a form instance with a name field of "Test Todo Items"
    - check that this instance is valid (even without selecting a "done" status)
1. test to ensure that the only fields that are displayed in the form are the "name" and "done" fields: `test_fields_are_explicit_in_form_metaclass`
    - create an empty form instance
    - check that the meta fields are equal to "name" and "done"

### Running tests

- run all tests: `python3 manage.py test`
- run a specific test e.g. form tests: `python3 manage.py test todo.test_forms`
- run a specific class of tests: `python3 manage.py test todo.test_forms.TestItemForm`
- run an individual test: `python3 manage.py test todo.test_forms.TestItemForm.test_fields_are_explicit_in_form_metaclass`

---

## Testing views in Django

### Testing objectives:
- check that the views return a successful HTTP response 
- check that they're using the proper templates
- check what they can do: adding, toggling and deleting items

### Creating the tests
- create the "test" file `"test_views.py"`
- import "TestCase" form "django.test" and "Item" from ".models"
- create a class `TestViews(TestCase):` that inherits "Testcase" and contain all the tests for the views
1. test that we can get the "todo_list" which is the home page
    - save the homepage instance as response
    - check that the response code is 200 (success)
    - check that the template used is `"todo/todo_list.html"`
1. test that we can get the "add_item" page
    - save the "add" instance as response
    - check that the response code is 200 (success)
    - check that the template used is `"todo/add_item.html"`
1. test that we can get the "edit_item" page
    - create an Item Object
    - save the response for that item
    - assert this item response code is 200
    - assert the template used is "edit_item.html"
1. test that we can add an item using the "add_item" view
    - create a new item
    - check it redirects to the home page
1. test that we can delete an item using the "delete_item" view
    - create a new item object instance
    - delete this item
    - assert that it redirects to the home page
    - try to return the item from the database using filter and the item_id
    - check the length of existing_items = 0
1. test we can toggle an item using the "toggle_item" view
    - create a new item object instance with done=True
    - toggle this item so done=False
    - assert that it redirects to the home page
    - get the item again and save as updated_item
    - check the done status is False

---

## Testing models

In general, we don't want to test internal Django code because it's already been tested by the Django developers themselves. But we can test that the todo items will be created by default with the done status of false.

- create the "test" file `"test_models.py"`
- import "TestCase" form "django.test" and "Item" from ".models"
- create a class `TestModels(TestCase):` that inherits "Testcase" and contain all the tests for the model
1. test that the todo items will be created by default with the done status of false
    - create a new item instance
    - check that item.done is False

---

## Coverage

Coverage is a tool that checks what percentage of the code is actually tested

- install the Coverage tool: `pip3 install coverage`
- run Coverage: `coverage run --source=todo manage.py test` - this generates the `.coverage` file
- view Coverage Report: `coverage report` 
- this report shows what percentage of the code is actually tested
- to see specifically what we're missing, Coverage allows us to create an interactive HTML report: `coverage html` - this creates the `htmlcov` folder
- view HTML Report: `python3 -m http.server`
- open the `.htmlcov` folder in the html directory
- the Coverage report shows that the application is not fully tested
    - in `models.py` we haven???t tested the string method of the item model

### Create the missing tests

1. in `models.py` test the "string" method of the item model
    - create a new item instance
    - assert the item's string is "Test Todo Item"
    - rerun Coverage
    - regenerate HTML Report
1. in `views.py` test the "POST" method
    - create a new item instance
    - edit the item using "POST" to "Updated Name"
    - check it redirects to home
    - save the edited item as updated_item
    - check this edited item equals "Updated Name"
    - rerun Coverage
    - regenerate HTML Report

*__Important__*
- the 100% coverage showed in the Coverage report does not mean that 100% of the tests pass, only that the code was tested 100%.
- run each test as it's written to reduce the chances of making an error
- if any tests fail, check the Error Messages

---

## Deployment

### Heroku Setup and CLI

Unfortunately, deploying to GitHub Pages won't work, since it can only handle front-end files such as HTML, CSS, and JavaScript. So the project needs to be deployed to a hosting platform that can render Python files. One such platform is [Heroku](https://id.heroku.com/login).

- sign up / login to [Heroku](https://id.heroku.com/login) website
- if necessary, install the heroku CLI in Gitpod: `curl https://cli-assets.heroku.com/install.sh | sh`
- login to Heroku CLI: `heroku login -i`

### Installing Project Requirements

Because Heroku uses an ephemeral file system, we can't use the local `db.sqlite3` database. We use instead a database called Postgres.

- install Postgres: `pip3 install psycopg2-binary`
- install webserver: `pip3 install gunicorn` - replaces the development server once the app is deployed to Heroku
- create a requirements file: `pip3 freeze --local > requirements.txt` - creates a file to let heroku know which packages to install

### Creating an Heroku App

- create the app in CLI: `heroku apps:create app-name --region eu`
- view theapps in CLI: `heroku apps`
- view the key remotes in CLI: `git remote -v`

### Creating a New Database on Heroku

The database is created on heroku website.

- in heroku app under the "Resources" tab, underneath the "Add-ons" section type `heroku postgress`
- choose `Hobby Dev - Free` option
- in "Settings" press "Reveal Config Vars" to see see that Heroku has created a DATABASE_URL for us to connect to from inside Django
- to see it in CLI type: "heroku addons"

*__Important__*

If you want to create this database with MySql instead of Postgres use DB add-on.

### Connecting to Our Remote Database

Set up the Django app to connect to the remote database.

- install a database url package: `pip3 install dj-database-url` - this package allows us to parse the database url that Heroku created
- refreeze the requirements file: `pip3 freeze --local > requirements.txt`
- get the url of the remote database in CLI: `heroku config -a app-name`
- in `settings.py` modify the original "DATABASE" settings to replace the value of the default database with the database url from Heroku
- import "dj_database_url"
- run migrations: `python3 manage.py migrate`
- update `.gitignore`
- add, commit and push

### Attempting a First Deployment

- deploy app to Heroku: `git push heroku main`
- if heroku repository is not find:
    - run `heroku git:remote -a app-name`
    - check remote repositories: `git remote -v`
    - redeploy the app to Heroku: `git push heroku main`
- open app - gives a "pre-receive hook declined" error caused by the fact that we don't have static files in the project
- to fix (pre-receive hook declined) disable Collect Static: `heroku config:set DISABLE_COLLECTSTATIC=1`
- redeploy the app to Heroku: `git push heroku main` - the app is pushed to heroku, but gives an error when trying to open it
- check the logs for errors: `heroku logs --tail`
- create a new file: `Procfile` and add `web: gunicorn django_todo.wsgi:application` to it - this tells gunicorn to run using our projects wsgi module
- add, commit and push
- open app - gives a "DisallowedHost" error
- to fix error, in `settings.py` add the host name of our Heroku app to `ALLOWED_HOSTS`
- add, commit and push

### Connecting Heroku to Github

By connecting Heroku to Github the application will automatically deploy the latest code to Heroku.

- in heroku app, open app, in "Deploy" tab, under the "Deployment method" setting select "GitHub"
- search for repository and click "Connect"
- choose "Enable Automatic Deploys"
- modify `settings.py` to use environment variables:
    - import os
    - get the Secret Key value using an environment variable
    - replace the Heroku host value in ALLOWED_HOSTS
    - replace the Database URL value in DATABASES
- add the environment variables to Heroku:
    - in heroku app, open app, in "Settings" tab press "Reveal Config Vars"
    - add new variable "HEROKU_HOSTNAME"
- confirm Heroku to Github connection:
    - update the titles of each template file
    - add, commit and push
    - refresh and check app

### The Development Environment

We need to set up a local development environment so that we don't have to change any settings to run our project in gitpod.

- modify `settings.py`:
    - create a new "development" variable
    - set "Debug" to development
    - modify the "DATABASES" configuration and add an if statement
- add a new environment variable set to TRUE
- restart workspace
- run server - the server starts, but we get a "DisallowedHost" error
- modify `settings.py` to fix it 
    - add a "localhost" as an ALLOWED_HOST if development = True
    - else use the HEROKU_HOSTNAME environment variable
- add, commit and push

### The SECRET_KEY

- in `settings.py` replace the default SECRET KEY with a blank string
- generate and copy a new Django Secret Key
- add a new environment variable
- restart the workspace
- create a Secret Key for Heroku
- add, commit and push

---

*Disclaimer: this is a code along project from [Code Institute's](https://codeinstitute.net/) **Hello Django** module*