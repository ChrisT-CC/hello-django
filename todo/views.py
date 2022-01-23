""" render web pages """
from django.shortcuts import render, redirect
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


def add_item(request):
    """
    creates a render for "add_item.html" template
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
