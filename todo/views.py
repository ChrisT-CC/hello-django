""" render web pages """
from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    """
    takes an http request from the user and return an http response to the
    user that says hello
    """
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
