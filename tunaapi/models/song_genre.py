"""Song database model module"""
from django.db import models
# need to import song and genre
from .song import Song
from .genre import Genre

class Song_Genre(models.Model):
    """Database model for keeping track of which songs belong to which genre"""
    # this song_id is the key from Song ID entity
    song_id =  models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_id')
    genre_id =  models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre_id')
