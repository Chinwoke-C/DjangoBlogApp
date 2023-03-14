from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, 'post/hello.html')


# def greet(request):
#     return HttpResponse("Welcome to Django class")


def greet(request):
    return render(request, 'post/greet.html')


def baby(request):
    return HttpResponse("I love software engineering")


def details(request):
    username = "chizzy"
    password = "big trees"
    return HttpResponse("my username is {username} and my password is {password}")
