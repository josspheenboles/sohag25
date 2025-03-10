from django.urls import path
from .views import *
urlpatterns=[
    path('',getalltrainees,name='trall'),
    path('/Add',addtrainees,name='tradd'),

]