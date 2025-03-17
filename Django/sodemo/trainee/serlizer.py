from rest_framework import serializers
from .models import Trainee
#model selizer --->modelform
class Trainee_serlizer(serializers.ModelSerializer):
    class Meta:
        model=Trainee
        fields='__all__'
