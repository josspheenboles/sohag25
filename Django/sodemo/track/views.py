from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def Listview(req):
    tracks=[
        [1,'python'],
        [2,'php'],
        [3,'Java'],
    ]
    # return HttpResponse('<h1>Tracks</h1>')
    return render(req,'track/list.html',context={
        'tracks':tracks
    })
@login_required()
def Addview(req):
    # return HttpResponse('<h1>add Track</h1>')
    return render(req,'track/new.html')
def Updateview(req,id):
    return HttpResponse(f'<h1>Updateview Track {id}</h1>')
def Deleteview(req,id):
    return HttpResponse(f'<h1>Deleteview Track {id}</h1>')
def findview(req,name):
    return HttpResponse(f'<h1>findview Track {name}</h1>')