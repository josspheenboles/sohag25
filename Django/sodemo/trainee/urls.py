from django.urls import path
from .views import *
urlpatterns=[
    path('',getalltrainees,name='trall'),
    # path('Add',addtrainees,name='tradd'),
    path('Add',TraineeViewAdd.as_view(),name='tradd'),
    # path('Update/<int:id>',updatetrainees,name='trupdate'),
    path('Update/<int:id>',TraineeViewupdate.as_view(),name='trupdate'),
    path('Delete/<int:id>',deletetrainees,name='trdelete'),

]