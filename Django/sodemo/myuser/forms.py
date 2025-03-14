from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput


class Useradd(UserCreationForm):
    age=forms.IntegerField(required=True)


from .models import *
class SigninForm(forms.ModelForm):
    class Meta:
        model=Usernative
        fields=['username','password']

class SignupForm(forms.ModelForm):
    password2=forms.CharField(required=True,widget=PasswordInput())
    class Meta:
        model=Usernative
        fields='__all__'