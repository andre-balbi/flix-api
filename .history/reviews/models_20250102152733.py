from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.PROTECT, related_name="reviews"
    )
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(max_length=300, null=True, blank=True)
