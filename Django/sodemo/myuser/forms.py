from django import forms
from django.contrib.auth.forms import UserCreationForm
class Useradd(UserCreationForm):
    age=forms.IntegerField(required=True)
