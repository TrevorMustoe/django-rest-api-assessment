"""Song database model module"""
from django.db import models
from .artists import Artists


class Song(models.Model):
    """Database model for keeping track of songs"""
    title = models.CharField(max_length=50)
    # this artist_id is the key from artist ID
    artist =  models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='song')
    album = models.CharField(max_length=50) 
    length = models.CharField(max_length=50) 