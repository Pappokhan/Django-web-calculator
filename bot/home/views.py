from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def index1(request):
    return render(request, "index1.html")
