from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer, ViewAlbumSerializer
from .models import Album

# Create your views here.

class AlbumsList(APIView):
    def get(self, _):
        albums = Album.objects.all()
        serializer = ViewAlbumSerializer(albums, many=True)
        if albums:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlbumDetails(APIView):
    def get(self, _, id):
        album = Album.objects.filter(id=id).first()
        serializer = ViewAlbumSerializer(album)
        if album:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        album = Album.objects.filter(id=id).first()
        serializer = AlbumSerializer(album, data=request.data)
        if album and serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, _, id):
        album = Album.objects.filter(id=id).first()
        if album:
            serializer = AlbumSerializer(album)
            album.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)