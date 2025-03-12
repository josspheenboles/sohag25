from django import forms
class Traineeadd(forms.Form):
    #input text
    name=forms.CharField(required=True,min_length=3,max_length=10)
