# Hello Django

This is a code along project to learn Django.

---

## Set up

- install Django: `pip3 install Django`
- create Django project: `django-admin startproject django_todo`
    - this will generate the project folder with a few ".py" files
    - `"__init__.py"` - tells our project that this is a directory we can import from
    - `"settings.py"` - contains globals settings for the entire Django project
        - whether we want to show debug information when errors happen
        - HTML templates location
        - which database we're going to connect to
    - `"urls.py"` -  contains the routing information that allows our users to type a specific URL into their address bar
        -  analogous to app.root in flask
    - `"wsgi.py"` - contains the code that allows our web server to communicate with our Python application
- run a Django project: `Python3 manage.py runserver`