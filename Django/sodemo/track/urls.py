from django.urls import path
from .views import *
urlpatterns=[path('Track/',Listview,name='tracks'),
    path('Track/Add',Addview,name='tracknew'),
    path('Track/Update/<int:id>',Updateview,name='trackupdate'),
    path('Track/Delete/<int:id>',Deleteview,name='trackdelete'),
    path('Track/<str:name>',findview,name='trackfind'),
]