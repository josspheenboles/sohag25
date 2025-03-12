from django.db import models
from track.models import Track2
from django.shortcuts import redirect
# Create your models here.
class Trainee(models.Model):
    #id auto,name,image,creatdate,email
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #image path upload image to it &
    image=models.ImageField(upload_to='trainee/images')
    createdate=models.DateTimeField(auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    #represent fk constrain
    # on update --->cascade
    # on delete --->cascade required
    #track is not int number in  database
    # in  models track is instance /object
    track=models.ForeignKey(to=Track2,on_delete=models.CASCADE)
    @classmethod
    def addtrainee(cls,name,email,image,trackid):
        Trainee.objects.create(name=name
                               , email=email
                               , image=image
                               # object of track2 model
                               , track=Track2.gettrackbyid(trackid))
    @classmethod
    def updatetrainee(cls,traineeid,name,email,image,trackid):
        Trainee.objects.filter(id=traineeid).update(name=name
                               , email=email
                               , image=image
                               # object of track2 model
                               , track=Track2.gettrackbyid(trackid))
    @staticmethod
    def gotoalltrainee():
        return redirect('trall')
    @classmethod
    def getallactivetrainee(cls):
        return cls.objects.filter(isactive=True)
    @classmethod
    def gettraineebyid(cls,id):
        return cls.objects.get(id=id)