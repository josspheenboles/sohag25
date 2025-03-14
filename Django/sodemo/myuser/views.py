from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Define view
# HttpResponse---doment.write
def Loginview(req):
    return  HttpResponse('<h1>login from view</h1>')
def logoutview(request):
    print(request,type(request))
    print(request.method)
    print(request.GET)
    obj=HttpResponse('<h1>hi</h1>')
    obj.write('<h2>hi</h2>')
    obj['content-type']='text/plain'
    return obj
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views import View
class RegViewCustom(View):
    def get(self,req):
        pass

    def post(self,req):
        pass

def Regview(req):
    context={'form':UserCreationForm()}
    if(req.method=='POST'):
        form=UserCreationForm(data=req.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('Login')
        else:
            context['msg']=form.errors
            return render(req, 'myuser/reg.html', context)
    return render(req, 'myuser/reg.html', context)