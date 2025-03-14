from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Trainee
from track.models import Track2
from .forms import Traineeadd,Traineeaddmodel
from django.http import HttpResponseRedirect,HttpResponse
import os
from django.conf import settings
#class based view
from django.views import View
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
# Create your views here.
#view list trainee
class TraineeShow(DetailView):
    model = Trainee
    context_object_name = 'trainee'

class TraineeList(ListView):
    model = Trainee
    template_name = 'trainee/list.html'
    context_object_name = 'trainees'
class TraineeViewAdd_G(CreateView):
    #generate form --->model--->insert operation
    model = Trainee
    template_name = 'trainee/addform.html'
    success_url = reverse_lazy('trall') #
    fields = '__all__'
    exclude = ['isactive']

class TraineeViewAdd(View):
    def get(self,request):
        context={'form':Traineeaddmodel()}
        return render(request,'trainee/addform.html',context)
    def post(self,request):
        #get data inserted by end user
        form=Traineeaddmodel(data=request.POST,files=request.FILES)
        if(form.is_bound and form.is_valid()):
            form.save()
            return Trainee.gotoalltrainee()
        else:
            context={'form':form,'error':form.errors}
            return render(request,'trainee/addform.html',context)

class TraineeViewupdate(View):
    def get(self,request,id):
        context={'form':Traineeaddmodel(instance=
            Trainee.gettraineebyid(id)
        )}
        return  render(request,'trainee/update.html',context)
    def post(self,request,id):
        form=Traineeaddmodel(data=request.POST,files=request.FILES,
                             instance=Trainee.gettraineebyid(id))
        if(form.is_bound and form.is_valid()):
            form.save()
            return Trainee.gotoalltrainee()
        else:
            context={'form':form,'error':form.errors}
            return render(request,'trainee/update.html',context)
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
    context={'form':Traineeaddmodel(instance=Trainee.gettraineebyid(id))}
    if(req.method=='POST'):
        #upload media asd.png--->uploading
        #upload media asd.png--->uploading asdrandomstr.png
        form=Traineeaddmodel(data=req.POST,files=req.FILES,instance=
                             Trainee.gettraineebyid(id))
        if(form.is_bound and form.is_valid()):
            form.save()#update
            return Trainee.gotoalltrainee()
        else:
            context['errors']=form.errors
            return render(req, 'trainee/update.html',context)
    return render(req, 'trainee/update.html',context)
def deletetrainees(req,id):
    #hard delete
    # Trainee.objects.filter(id=id).delete()
    #soft deleet
    Trainee.objects.filter(id=id).update(isactive=False)
    # return HttpResponseRedirect('/Trainee/')
    return  redirect('trall')