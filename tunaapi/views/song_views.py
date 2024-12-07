"""View module for handling requests about song"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song


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
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length')