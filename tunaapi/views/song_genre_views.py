"""View module for handling requests about song_genre"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song_Genre


class Song_GenreView(ViewSet):
    """Tuna Api Song_genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song_genre

        Returns:
            Response -- JSON serialized song_genre
        """
        song_genre = Song_Genre.objects.get(pk=pk)
        serializer = Song_GenreSerializer(song_genre)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all song_genres

        Returns:
            Response -- JSON serialized list of song_genres
        """
        
        song_genre = Song_Genre.objects.all()
        serializer = Song_GenreSerializer(song_genre, many=True)
        return Response(serializer.data)   
class Song_GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for song_genre
    """
    class Meta:
        model = Song_Genre
        fields = ('id', 'song_id', 'genre_id')