from rest_framework import serializers
from .models import Track2
class Track_serlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)#pk
    name=serializers.CharField(max_length=50)

    @classmethod
    def translatealltracktojson(cls):
        tracks = Track2.objects.all()
        tracks_serlized = Track_serlizer(tracks, many=True)
        return tracks_serlized.data