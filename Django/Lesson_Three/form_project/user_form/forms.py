from django import forms
from .models import User


class UserForm(forms.ModelForm):
    """form with models"""
    class Meta:
        model = User
        fields = "__all__"






















#custom validator
#custom validator should be defined with 1 argument which is value
# def check_mail(value):
#     """validate email is a gmail acct"""
#     if not value.endswith("@gmail.com"):
#         raise forms.ValidationError("Use a gmail account")


# class UserForm(forms.Form):
#     """simple user form"""
#     name = forms.CharField()
#     email = forms.EmailField(validators=[check_mail])
#     verify_email = forms.EmailField(label="Verify Email")
#     text = forms.CharField(widget=forms.Textarea)
#     # using built in validator to make sure only integers are inputed
#     age = forms.CharField(validators=[validators.integer_validator])

#     def clean(self):
#         all_data = super().clean()

#         if all_data.get('email') != all_data.get('verify_email'):
#             raise forms.ValidationError("Emails do not match")

