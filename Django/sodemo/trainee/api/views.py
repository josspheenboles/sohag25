from django.template.context_processors import request

from .serlizer import Trainee_serlizer
from rest_framework import generics
from ..models import Trainee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
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
      #get data
      #serlization
      trainee_ser_object=Trainee_serlizer(data=request.data)
      #valid
      if(trainee_ser_object.is_valid()):
         #response
         trainee_ser_object.save()
         return Response(data=trainee_ser_object.data,
                         status=status.HTTP_201_CREATED)

class Trainee_Update_Delete_GETbyid(APIView):
   #return for trainee with this pk
   def get(self,request,pk):
      object=Trainee_serlizer.gettraineebyid(pk)
      return Response(
          data=object,
          status=status.HTTP_200_OK
       )
   #update for specific field
   def put(self,request,pk):
      #getoldinstance
      oldobj=get_object_or_404(Trainee,id=pk)
      #getdata selization & pass old object
      objserlized=Trainee_serlizer(data=request.data,instance=oldobj)
      #validat
      if(objserlized.is_valid()):
         #save
         objserlized.save()
         #response
         return Response(
            data=objserlized.data,
            status=status.HTTP_200_OK
         )
      else:
         return Response(data=
                         {
                            'errors':objserlized.errors
                         })
   def delete(self,request,pk):
      # getoldinstance
      oldobj = get_object_or_404(Trainee, id=pk)
      oldobj.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

# class Trainee_List_Creat(generics.ListCreateAPIView):
#    queryset = Trainee.getallactivetrainee()
#    serializer_class = Trainee_serlizer
#
#
# class Trainee_Update_Delete_GETbyid(generics.RetrieveAPIView):
#    queryset = Trainee.getallactivetrainee()
#    serializer_class = Trainee_serlizer
