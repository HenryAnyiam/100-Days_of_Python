from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def index(request):
    """home page"""
    return render(request, "base_app/index.html")

def sign_up(request):
    """user sign up"""

    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)

            if 'profile_pic' in request.FILES:
                user.profile_pic = request.FILES['profile_pic']
            user.save()            
        else:
            print(user_form.errors)
            return render(request, "base_app/sign_up.html",
                  {'user':user_form,})
    user_form = UserForm()
    return render(request, "base_app/sign_up.html",
                  {'user':user_form,})
