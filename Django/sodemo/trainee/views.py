from django.shortcuts import render

# Create your views here.
def getalltrainees(req):
    return render(req,'trainee/list.html')