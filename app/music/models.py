from django.db import models
from app.album.models import Album

# Create your models here.

class Songs(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='songs', null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
    
    def __str__(self):
        return self.name
    