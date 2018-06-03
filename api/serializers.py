from rest_framework import serializers
from api.models import PhotoReact


class PhotoReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoReact
        fields = ('id', 'photo_react', 'name', 'created', 'latitud', 'longitud')

