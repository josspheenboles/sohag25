from rest_framework import serializers
from trainee.models import Trainee
#model selizer --->modelform
class Trainee_serlizer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'
    @classmethod
    def getallactive(cls):
        return  cls(Trainee.getallactivetrainee(),many=True).data