from rest_framework import serializers
from api.models import PhotoReact


class PhotoReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoReact
        fields = ('id', 'photo_react', 'photo_react_thumbnail_url', 'name', 'created', 'latitud', 'longitud')

