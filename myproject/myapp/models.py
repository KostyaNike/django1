from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, related_name='games')
    release_year = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title