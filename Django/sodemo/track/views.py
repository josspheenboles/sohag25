from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Listview(req):
    return HttpResponse('<h1>Tracks</h1>')
def Addview(req):
    return HttpResponse('<h1>add Track</h1>')
def Updateview(req,id):
    return HttpResponse('<h1>Updateview Track</h1>')