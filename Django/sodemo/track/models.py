from django.db import models

# Create your models here.
#model Track
class Track(models.Model):
    #prop
    #id int autoincrement pk
    id=models.AutoField(primary_key=True,db_column='trackid')
    #name varchar 50
    name=models.CharField(max_length=50,null=False,unique=True)