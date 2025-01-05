from django.db import models
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,  # This parameter ensures that if a genre is deleted, its associated movies will not be deleted.
        related_name="movies",  # Whenever creating a foreign key, include a related_name, as it simplifies future queries.
    )
    actors = models.ManyToManyField(
        "actors.Actor",
        related_name="movies",
        blank=True,
    )
    resume = models.TextField()

    # The __str__ method is a special method in Python that returns a string representation of an object.
    def __str__(self):
        return self.title
