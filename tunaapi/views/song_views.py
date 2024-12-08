"""View module for handling requests about song"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artists,Genre


class SongView(ViewSet):
    """Tuna Api Song view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single song type
        
        Returns:
            Response -- JSON serialized song type
        """
        try:
            song = Song.objects.get(pk=pk)
            genres = Genre.objects.filter(genre_id__song_id=song)
            song.genres=genres.all()
            serializer = SingleSongSerializer(song)
            return Response(serializer.data)
        except Song.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

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
    
    def update(self, request, pk):
        """Handle PUT requests for a song

        Returns:
            Response -- Empty body with 204 status code
        """

        song = Song.objects.get(pk=pk)
        song.title = request.data["title"]
        song.album = request.data["album"]
        song.length = request.data["length"]

        artist = Artists.objects.get(pk=request.data["artist"])
        song.artist_id = artist
        song.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song types
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'length')
        depth = 1

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('id', 'description')
        depth = 1

class SingleSongSerializer(serializers.ModelSerializer):
  """JSON serializer for song types
    """
  genres = GenreSerializer(read_only=True, many=True)
  class Meta:
      model = Song
      fields = ('id', 'title', 'artist', 'album', 'length', 'genres')
      depth = 2