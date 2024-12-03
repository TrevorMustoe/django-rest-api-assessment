"""Genere database model module"""
from django.db import models


class Genre(models.Model):
    """Database model for tracking different types of generes"""
    desription = models.CharField(max_length=50)