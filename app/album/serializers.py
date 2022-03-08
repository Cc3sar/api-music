from rest_framework import serializers
from app.music.serializers import SongSerializer
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = (
            "id",
        )

class ViewAlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = "__all__"
        read_only_fields = (
            "id",
        )