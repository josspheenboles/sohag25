from rest_framework import serializers
from trainee.models import Trainee
from django.shortcuts import get_object_or_404,get_list_or_404
#model selizer --->modelform
class Trainee_serlizer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'
    @classmethod
    def getallactive(cls):
        return  cls(Trainee.getallactivetrainee(),many=True).data

    @classmethod
    def gettraineebyid(cls,id):

        return cls(get_object_or_404(Trainee,id=id)).data

