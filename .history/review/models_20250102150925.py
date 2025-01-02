from django.db import models


class Review(models.Model):
    movie = (
        models.ForeignKey(
            "movies.Movie", on_delete=models.PROTECT, related_name="reviews"
        ),
    )
    rating = models.IntegerField(validators=[models.Min(0), models.Max(10)])
