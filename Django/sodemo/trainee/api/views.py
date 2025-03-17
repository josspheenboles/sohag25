from .serlizer import Trainee_serlizer
from rest_framework import generics
from ..models import Trainee

class Trainee_List_Creat(generics.ListCreateAPIView):
   queryset = Trainee.getallactivetrainee()
   serializer_class = Trainee_serlizer

class Trainee_Update_Delete_GETbyid(generics.RetrieveAPIView):
   queryset = Trainee.getallactivetrainee()
   serializer_class = Trainee_serlizer