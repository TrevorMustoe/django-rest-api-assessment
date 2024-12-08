"""View module for handling requests about genre"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):
    """Tuna Api Genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Genre

        Returns:
            Response -- JSON serialized Genre
        """
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

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
     
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for genre
    """
    class Meta:
        model = Genre
        fields = ('id', 'description')