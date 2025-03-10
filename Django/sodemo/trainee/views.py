from django.shortcuts import render
from .models import Trainee
# Create your views here.
def getalltrainees(req):
    return render(req,'trainee/list.html')
def addtrainees(req):
    if(req.method=='POST'):
        #get info
        trname=req.POST['trname']
        tremail=req.POST['tremail']
        trimg=req.FILES['trimg']
        #save db
        obj=Trainee(name=trname,email=tremail,image=trimg)
        obj.save()
    return render(req,'trainee/add.html')
def updatetrainees(req,id):
    return render(req, 'trainee/update.html')
def deletetrainees(req,id):
    return render(req,'trainee/list.html')