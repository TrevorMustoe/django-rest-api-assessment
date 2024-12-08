"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artists, Song


class ArtistsView(ViewSet):
    """Tuna Api Artists view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single artists

        Returns:
            Response -- JSON serialized artists
        """
        artists = Artists.objects.get(pk=pk)
        serializer = ArtistsSerializer(artists)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all artistss

        Returns:
            Response -- JSON serialized list of artistss
        """
        
        artists = Artists.objects.all()
        serializer = ArtistsSerializer(artists, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized artist instance
        """

        artist = Artists.objects.create(
            name=request.data["name"],
            age=request.data["age"],
            bio=request.data["bio"],
        )
        serializer = ArtistsSerializer(artist)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a artist

        Returns:
            Response -- Empty body with 204 status code
        """

        artist = Artists.objects.get(pk=pk)
        artist.name = request.data["name"]
        artist.age = request.data["age"]
        artist.bio = request.data["bio"]

        artist.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        artist = Artists.objects.get(pk=pk)
        artist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ArtistsSerializer(serializers.ModelSerializer):
    """JSON serializer for artists
    """
    class Meta:
        model = Artists
        fields = ('id', 'name', 'age', 'bio')
