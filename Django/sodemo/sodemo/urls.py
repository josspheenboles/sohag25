"""
URL configuration for sodemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myuser.views import *
from track.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #route my user app
    path('Login/',Loginview,name='Login'),
    path('Logout/',logoutview,name='Logout'),
    path('Reg/',Regview,name='Reg'),
    #routes track app
    path('Track/',Listview,name='tracks'),
    path('Track/Add',Addview,name='tracknew'),
    path('Track/Update',Updateview,name='trackupdate'),

]
