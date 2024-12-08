"""View module for handling requests about song"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artists


class SongView(ViewSet):
    """Tuna Api Song view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song

        Returns:
            Response -- JSON serialized song
        """
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songs

        Returns:
            Response -- JSON serialized list of songs
        """
        
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized artist instance
        """
        artist = Artists.objects.get(pk=request.data["artist"])

        artist = Song.objects.create(
            title=request.data["title"],
            artist=artist,
            album=request.data["album"],
            length=request.data["length"],
        )
        serializer = SongSerializer(artist)
        return Response(serializer.data) 
    
    def destroy(self, request, pk):
        artist = Song.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  
        
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length')