from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def Listview(req):
    tracks=[
        [1,'python'],
        [2,'php'],
        [3,'Java'],
    ]
    # return HttpResponse('<h1>Tracks</h1>')
    return render(req,'track/list.html',context={
        'tracks':tracks
    })
@login_required()
def Addview(req):
    # return HttpResponse('<h1>add Track</h1>')
    return render(req,'track/new.html')
def Updateview(req,id):
    return HttpResponse(f'<h1>Updateview Track {id}</h1>')
def Deleteview(req,id):
    return HttpResponse(f'<h1>Deleteview Track {id}</h1>')
def findview(req,name):
    return HttpResponse(f'<h1>findview Track {name}</h1>')

#===================== API =======================
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serlizer import Track_serlizer

#list track & add new track
@api_view(['GET','POST'])
def List_Create_Track(request):
    if(request.method=='GET'):
        return Response(data=Track_serlizer.translatealltracktojson(),status=status.HTTP_202_ACCEPTED)
    elif(request.method=='POST'):
        #de serlizer convert from json to objcte of Track_serlizer
        track_selized_object=Track_serlizer(data=request.data)
        print(track_selized_object)#objct of track_serlizer
        if(track_selized_object.is_valid()):
            track_selized_object.save()
            return Response(data=track_selized_object.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def hellowrld(req):

    jsonobj={'api':
                 {
                     'list':'Track/API/ & get mthod',
                     'insert':'Track/API/ & post mthod',
                     'delelte':'Track/API/<int:id> & delete mthod',
                     'updatefull':'Track/API/<int:id> & put mthod',
                     'updatepartial':'Track/API/<int:id> & patch mthod',
                     'viewdetails':'Track/API/<int:id> & get mthod',

                 }}
    return Response(data=jsonobj,status=status.HTTP_201_CREATED)



