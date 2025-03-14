from django.db import models
from track.models import Track2
from django.shortcuts import redirect
import os

def user_directory_path(instance, filename):
    # Upload files to "media/profile_images/{id}/{filename}"
    return f'trainee/images/{instance.id}/{filename}'
# Create your models here.
class Trainee(models.Model):
    #id auto,name,image,creatdate,email
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #image path upload image to it &    j
    image=models.ImageField(upload_to='trainee/images/')
    createdate=models.DateTimeField(auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)
    isactive=models.BooleanField(default=True)
    #represent fk constrain
    # on update --->cascade
    # on delete --->cascade required
    #track is not int number in  database
    # in  models track is instance /object
    track=models.ForeignKey(to=Track2,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Delete old image if a new one is uploaded
        if self.pk:
            old_profile = Trainee.objects.filter(pk=self.pk).first()
            if old_profile and old_profile.image and old_profile.image != self.image:
                old_image_path = os.path.join(old_profile.image.path)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        #not db
        super().save(*args, **kwargs)  # ✅ Ensures correct upload path

    @classmethod
    def addtrainee(cls,name,email,image,trackid):
        Trainee.objects.create(name=name
                               , email=email
                               , image=image
                               # object of track2 model
                               , track=Track2.gettrackbyid(trackid))
    @classmethod
    def updatetrainee(cls,traineeid,name,email,myimage,trackid,traineeobj):
        # print(image,type(image))
        cls.objects.filter(id=traineeid).update(name=name
                               , email=email
                               , image=myimage
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

    def getimageurl(self):
        return '/media/'+self.image
