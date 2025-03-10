from django.shortcuts import render

# Create your views here.
def getalltrainees(req):
    return render(req,'trainee/list.html')
def addtrainees(req):
    return render(req,'trainee/add.html')
def updatetrainees(req,id):
    return render(req, 'trainee/update.html')