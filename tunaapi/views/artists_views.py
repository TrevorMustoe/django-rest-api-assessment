"""View module for handling requests about artists"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Artists


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
class ArtistsSerializer(serializers.ModelSerializer):
    """JSON serializer for artists
    """
    class Meta:
        model = Artists
        fields = ('id', 'name', 'age', 'bio')