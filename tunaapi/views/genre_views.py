"""View module for handling requests about genre"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre, Song, Song_Genre


class GenreView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for a single Genre with its songs"""
        try:
            # This gets the genre
            genre = Genre.objects.get(pk=pk)
            
            # This finds the song ID assosicated with the genre that is selected
            song_genres = Song_Genre.objects.filter(genre_id=pk)
            song_ids = song_genres.values_list("song_id", flat=True)
            
            # This is what actually gets the song details and joins the primary key of song
            # The primary key __in from the data of song_ids
            songs = Song.objects.filter(pk__in=song_ids)
            
            # Serialize!!
            genre_data = GenreSerializer(genre).data
            
            # Serialize the associated songs and add them to the genre data
            genre_data["songs"] = SongSerializer(songs, many=True).data
            
            return Response(genre_data, status=status.HTTP_200_OK)
        except Genre.DoesNotExist:
            return Response(
                {"message": "Genre not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def list(self, request):
        """Handle GET requests to get all genres

        Returns:
            Response -- JSON serialized list of genres
        """
        
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized artist instance
        """

        artist = Genre.objects.create(
            description=request.data["description"],
        )
        serializer = GenreSerializer(artist)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        artist = Genre.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  
    
    def update(self, request, pk):
        """Handle PUT requests for a genre

        Returns:
            Response -- Empty body with 204 status code
        """

        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]

        genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
     
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genre
    """
    class Meta:
        model = Genre
        fields = ('id', 'description')
        
class SongSerializer(serializers.ModelSerializer):
    """JSON serializer for song
    """
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist', 'album', 'length')