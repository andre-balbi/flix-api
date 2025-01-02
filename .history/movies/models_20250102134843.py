from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ForeignKey("genres.Genre", on_delete=models.PROTECT)
    poster = models.CharField(max_length=200, blank=True, null=True)
