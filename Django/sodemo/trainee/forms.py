from curses.textpad import Textbox
from django import forms
from django.forms import TextInput
from track.models import Track2
from .models import Trainee
class Traineeaddmodel(forms.ModelForm):
    class Meta:
        modle=Trainee
class Traineeadd(forms.Form):
    #input text
    trname=forms.CharField(
        label='Full Name',
        required=True,min_length=3,max_length=10,
    )
    tremail=forms.EmailField(label='Email')
    trimg=forms.ImageField(label='Profile Image')
    #choises tuple of tuples
    trtrack=forms.ChoiceField(widget=forms.SelectMultiple,
        choices=[(track.id,track.name) for track in Track2.getalltracks()]
    )
    # test=forms.DateTimeField()