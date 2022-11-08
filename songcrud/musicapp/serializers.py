from rest_framework import serializers
from .models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class SongOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'artiste_id.first_name', 'date_released', 'likes')