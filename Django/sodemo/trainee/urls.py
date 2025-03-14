from django.urls import path
from .views import *
urlpatterns=[
    # path('',getalltrainees,name='trall'),
    path('',TraineeList.as_view(),name='trall'),
    path('Show/<pk>',TraineeShow.as_view(),name='trshow'),
    # path('Add',addtrainees,name='tradd'),
    # path('Add',TraineeViewAdd.as_view(),name='tradd'),
    path('Add',TraineeViewAdd_G.as_view(),name='tradd'),
    # path('Update/<int:id>',updatetrainees,name='trupdate'),
    path('Update/<int:id>',TraineeViewupdate.as_view(),name='trupdate'),
    path('Delete/<int:id>',deletetrainees,name='trdelete'),

]