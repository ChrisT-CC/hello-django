""" render web pages """
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    """
    creates a render for "edit_item.html" template
    """
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    """
    creates a render for toggling an item
    """
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    """
    creates a render for deleting an item
    """
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
