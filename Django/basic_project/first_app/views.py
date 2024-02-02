from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, name):
    """simple view"""
    return render(request,
                  'first_app/index.html',
                  {"name": name,
                   "request": request})


def display(request):
    """picture"""
    return render(request, 'first_app/display.html')