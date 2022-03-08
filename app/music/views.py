from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Songs

# Create your views here.

class SongsList(APIView):
    def get(self, _):
        songs = Songs.objects.all()
        serializer = SongSerializer(songs, many=True)
        if songs:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SongDetails(APIView):
    def get(self, _, id):
        song = Songs.objects.filter(id=id).first()
        serializer = SongSerializer(song)
        if song:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        song = Songs.objects.filter(id=id).first()
        serializer = SongSerializer(song, data=request.data)
        if song and serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, _, id):
        song = Songs.objects.filter(id=id).first()
        if song:
            serializer= SongSerializer(song)
            song.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)