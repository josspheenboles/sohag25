from django.template.context_processors import request

from .serlizer import Trainee_serlizer
from rest_framework import generics
from ..models import Trainee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#function based 2 function
#function handel --->getall,cretae
#function handel --->getbyid,updtaebyid,delete byid

#class based view
class Trainee_List_Creat(APIView):
   def get(self,request):
      return Response(
         data=Trainee_serlizer.getallactive(),
         status=status.HTTP_200_OK
      )
   def post(self,request):
      pass

class Trainee_Update_Delete_GETbyid(APIView):
   pass
# class Trainee_List_Creat(generics.ListCreateAPIView):
#    queryset = Trainee.getallactivetrainee()
#    serializer_class = Trainee_serlizer
#
#
# class Trainee_Update_Delete_GETbyid(generics.RetrieveAPIView):
#    queryset = Trainee.getallactivetrainee()
#    serializer_class = Trainee_serlizer
