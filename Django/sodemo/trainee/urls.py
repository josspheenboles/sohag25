from django.urls import path, include
from .views import *
from .api.views import *
#router simple,default
from rest_framework import routers
#simple router--->crud

#default router--->help,prefix json or xml,crud,auth,

r=routers.DefaultRouter()
r.register(r'API',TraineeView)

urlpatterns=[
    # path('',getalltrainees,name='trall'),
    # path('',TraineeList.as_view(),name='trall'),
    # path('Show/<pk>',TraineeShow.as_view(),name='trshow'),
    # path('Add',addtrainees,name='tradd'),
    # # path('Add',TraineeViewAdd.as_view(),name='tradd'),
    # # path('Add',TraineeViewAdd_G.as_view(),name='tradd'),
    # path('Update/<int:id>',updatetrainees,name='trupdate'),
    # # path('Update/<int:id>',TraineeViewupdate.as_view(),name='trupdate'),
    # path('Delete/<int:id>',deletetrainees,name='trdelete'),
    # # path('API/',TraineeView.as_view()),
    # # path('API/',Trainee_List_Creat.as_view()),
    # path('API/<pk>/',Trainee_Update_Delete_GETbyid.as_view()),
    path('',include(r.urls)),

]