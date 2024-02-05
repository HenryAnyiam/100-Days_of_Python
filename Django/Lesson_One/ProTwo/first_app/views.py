from django.shortcuts import render
from first_app.models import *

# Create your views here.

def users(request):
    users = User.objects.all()
    return render(request, 'first_app/user.html',
                  {'users': users})

def index(request):
    return render(request, "first_app/index.html")