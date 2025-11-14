from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50, null=False)
    MOVIE_GENRES = {
        ('A', 'Acción'),
        ('D', 'Drama'),
        ('R', 'Romance'),
        ('C', 'Comedia'),
        ('T', 'Terror'),
        ('I', 'Infantil')
    }
    genre = models.CharField(max_length=30, choices=MOVIE_GENRES, null=False)
    director = models.CharField(max_length=30, null=False)
    release_year = models.IntegerField(null=False)
    synopsis = models.TextField(null=True)
    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.title

