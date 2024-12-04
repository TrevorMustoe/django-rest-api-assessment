"""Artists database model module"""
from django.db import models


class Artists(models.Model):
    """Database model for keeping track of artist information"""
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)