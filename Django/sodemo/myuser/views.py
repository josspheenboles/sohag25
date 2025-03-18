from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from .forms import *
from .models import Usernative
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#====================rest re
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serlizer import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .utils import accouttoken

@api_view(['POST'])
def customreg(request):
    #get data &deserlization
    serlizedoobj=CustomuserSerlizer(data=request.data)
    #validate
    if(serlizedoobj.is_valid()):
    #if valids
        # save
        user=serlizedoobj.save()
        subject='thnx for registration ,kindly verified'
        message=render_to_string(
            'myuser/veemail.html',
            {
                'user':user,
                'domain':request.get_host(),
                'uid':urlsafe_base64_decode(force_bytes(user.pk)),
                'token':accouttoken.make_token(user),
            }        )
        try:
            send_mail(subject,message,'norelpay@gmail.com',[user.email])
            return Response(
                data=CustomuserSerlizer(instance=user).data,
                status=status.HTTP_201_CREATED
            )
        except:
            #else &delete just savd user
            user.delete()
            return Response(
                data={'msg':'fake email'},
                status=status.HTTP_400_BAD_REQUEST
            )
    #else
    else:
        return Response(
            data={'errors':serlizedoobj.errors},
                  status=status.HTTP_400_BAD_REQUEST
        )
from django.shortcuts import get_object_or_404
@api_view(['GET'])
def verifiy_email(request):
    #get data
    uid=force_str(urlsafe_base64_decode(request.data['uidb64']))
    token=request.data['token']
    user=get_object_or_404(CustomUser,id=uid)
    if(user is not None
            and accouttoken.check_token(token)):
        user.email_ver=True
        user.save()
        return Response(
            data={'msg':'verification done'},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            data={'msg': 'invalid token url done'},
            status=status.HTTP_406_NOT_ACCEPTABLE
        )





class SignOutView(View):
    def get(self,req):
        req.session.clear()
        logout(req)
        return redirect('Loginnative')

class Signin(View):
    def get(self,req):
        context={'form':SigninForm()}
        return render(req,'nativr/login.html',context)
    def post(self,req):
        logeduserobj=Usernative.objects.filter(
            username=req.POST['username'],
            password=req.POST['password']).first()
        loggedauthuserobj=authenticate(
                username=req.POST['username'],
                password=req.POST['password'])
        if(logeduserobj is not None and loggedauthuserobj):
            ##sesion
            req.session['id']=logeduserobj.id
            req.session['name']=logeduserobj.username
            login(req)
            return redirect('trall')
        else:
            context={'msg':'invalid username or password'}
            return render(req, 'nativr/login.html', context)


class Signup(View):
    def get(self,req):
        context={'form':SignupForm()}
        return render(req,'nativr/reg.html',context)
    def post(self,req):
        form=SignupForm(data=req.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            User.objects.create_user(username=form.clean_data['username'],
                                     password=form.clean_data['password'],
                                     isactive=True)
            return redirect('Loginnative')
        else:
            context={
                'form':form,
                'msg':form.errors
            }
            return render(req, 'nativr/reg.html', context)



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
from .forms import Useradd
from django.shortcuts import redirect
from django.views import View
from .models import Myuser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class RegViewCustom(View):
    def get(self,req):
        context={'form':Useradd()}
        return render(req,'myuser/reg.html',context)

    def post(self,req):
        form=Useradd(data=req.POST)
        # print(form.cleaned_data)
        # print(form.cleaned_data['age'])
        if(form.is_bound and form.is_valid() and

        int(form.cleaned_data['age'])>21):
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                                     )
            Myuser.objects.create(age=form.cleaned_data['age'],
                                  username=form.cleaned_data['username'])
        else:
            context={'msg':'age must > 21','form':form}
            return render(req, 'myuser/reg.html', context)

from django.contrib.auth.forms import UserCreationForm
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