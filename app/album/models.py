from django.db import models

# Create your models here.

class Album (models.Model):
    name = models.CharField(max_length=150)
    nameband = models.CharField(max_length=150)
    date = models.DateField()

    class Meta:
        verbose_name = "Album",
        verbose_name_plural = "Albums"
    
    def __str__(self):
        return self.name