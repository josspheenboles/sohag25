from rest_framework import serializers
from .models import CustomUser
class CustomuserSerlizer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'