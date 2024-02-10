from django import forms
from .models import User

class UserForm(forms.ModelForm):
    """form foe the user"""

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'profile_pic', 'portfolio_link')
