from django.db import models

# Create your models here.
class Trainee(models.Model):
    #id auto,name,image,creatdate,email
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    #image path upload image to it &
    # image=models.ImageField()
    createdate=models.DateTimeField(auto_now_add=True)
    updateddate=models.DateTimeField(auto_now=True)
