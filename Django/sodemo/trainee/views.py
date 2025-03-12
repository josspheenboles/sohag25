from django.shortcuts import render,redirect
from .models import Trainee
from track.models import Track2
from .forms import Traineeadd,Traineeaddmodel
from django.http import HttpResponseRedirect
# Create your views here.

def getalltrainees(req):
    context={}
    #select * from trianee_trainees
    # context['trainees']=Trainee.objects.all()
    context['trainees']=Trainee.getallactivetrainee()
    return render(req,'trainee/list.html',context)
def addtrainees(req):
    context={'tracks':Track2.getalltracks(),
             'form':Traineeaddmodel()}

    if(req.method=='POST' ):
        form=Traineeaddmodel(data=req.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            # Trainee.addtrainee(req.POST['trname']
            #                        ,req.POST['tremail']
            #                        ,req.FILES['trimg']
            #                        #object of track2 model
            #                        ,req.POST["trtrack"])
            return Trainee.gotoalltrainee()
        else:
            context['error']=form.errors
            return render(req, 'trainee/addform.html', context)
    return render(req,'trainee/addform.html',context)
def updatetrainees(req,id):
    context={'oldobj':Trainee.gettraineebyid(id=id),
             'tracks':Track2.getalltracks()}
    if(req.method=='POST'):
        Trainee.updatetrainee(traineeid=id,
        name=req.POST['trname'],
        email=req.POST['tremail'],
        image=req.FILES['trimg'],
        trackid=req.POST['trtrack']
        )
        return  Trainee.gotoalltrainee()
    return render(req, 'trainee/update.html',context)
def deletetrainees(req,id):
    #hard delete
    # Trainee.objects.filter(id=id).delete()
    #soft deleet
    Trainee.objects.filter(id=id).update(isactive=False)
    # return HttpResponseRedirect('/Trainee/')
    return  redirect('trall')