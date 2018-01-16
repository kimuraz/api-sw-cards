from django.db import models


class Card(models.Model):
    """Card model representation."""
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    photo_url = models.URLField(null=False, blank=False)
    planet = models.CharField(max_length=30, null=False, blank=False)
