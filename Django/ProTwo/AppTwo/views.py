from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """simple index"""
    return HttpResponse("<em>My Second App</em>")

def help(request):
    """help page"""
    return render(request,
                  "AppTwo/index.html",
                  {"help": "Help Page"})