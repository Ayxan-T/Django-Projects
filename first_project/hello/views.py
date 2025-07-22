from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def aykhan(request):
    return HttpResponse("Hello, Aykhan!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })

def adder(request, a, b):
    return render(request, "hello/adder.html", {
        "A" : a,
        "B" : b,
        "sum": a + b
    })