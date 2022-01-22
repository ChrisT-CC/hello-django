""" render web pages """
from django.shortcuts import render, HttpResponse


# Create your views here.
def say_hello(request):
    """
    takes an http request from the user and return an http response to the
    user that says hello
    """
    return HttpResponse("Hello!")
