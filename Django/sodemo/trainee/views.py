from django.shortcuts import render,redirect
from .models import Trainee
from track.models import Track2
from .forms import Traineeadd,Traineeaddmodel
from django.http import HttpResponseRedirect
import os
from django.conf import settings
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
        form=Traineeaddmodel(data=req.POST,files=req.FILES)
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
    oldobj=Trainee.gettraineebyid(id=id)
    context={'oldobj':oldobj,
             'tracks':Track2.getalltracks()}
    print('----',req.method)
    if(req.method=='POST'):
        # Assign new image and save
        if oldobj.image:
            old_image_path ='media/trainee/images/'+str(oldobj.image)
            print(os.path.exists(old_image_path))
            if os.path.exists(old_image_path):
                os.remove(old_image_path)
                print('removed')
        Trainee.updatetrainee(traineeid=id,
        name=req.POST['trname'],
        email=req.POST['tremail'],
        myimage=req.FILES['trimg'],
        trackid=req.POST['trtrack']
        )
        oldobj.image=req.FILES['trimg']
        oldobj.save()
        return  Trainee.gotoalltrainee()
    return render(req, 'trainee/update.html',context)
def deletetrainees(req,id):
    #hard delete
    # Trainee.objects.filter(id=id).delete()
    #soft deleet
    Trainee.objects.filter(id=id).update(isactive=False)
    # return HttpResponseRedirect('/Trainee/')
    return  redirect('trall')