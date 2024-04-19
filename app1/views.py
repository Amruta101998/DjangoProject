from django.shortcuts import render
# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')


def index(request):
    return HttpResponse("Hello, this is your app's index view.")

# Create your views here.
def home(request):
    return render(request,'home.html')


def index(request):
    return HttpResponse("Hello, this is your app's index view.")
