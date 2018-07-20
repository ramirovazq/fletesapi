from rest_framework import serializers
from api.models import PhotoReact, LimeDemo


class PhotoReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhotoReact
        fields = ('id', 'photo_react', 'photo_react_thumbnail_url', 'name', 'created', 'latitud', 'longitud')



class LimeDemoSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(allow_blank=True)
    api_consulting = serializers.CharField(max_length=33, allow_blank=False, trim_whitespace=True)
    name = serializers.CharField(max_length=80, allow_blank=True, trim_whitespace=True)
    class Meta:
        model = LimeDemo
        fields = ('created', 'email', 'api_consulting', 'name', 'token')

