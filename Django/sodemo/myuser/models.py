from django.db import models

# Create your models here.
class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    age=models.IntegerField()
    username=models.CharField(max_length=100)