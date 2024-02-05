from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
    return render(request, "user_form/index.html")

def user(request):
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print(f"Name: {user_form.cleaned_data['name']}")
            print(f"EMAIL: {user_form.cleaned_data['email']}")
            print(f"TEXT: {user_form.cleaned_data['text']}")
            user_form.save()
    user_form = UserForm()
    return render(request, "user_form/form.html", {"form": user_form})
