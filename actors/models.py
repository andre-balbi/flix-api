from django.db import models


NATIONALITY_CHOICES = (
    ("United States", "United States"),
    ("Canada", "Canada"),
    ("Mexico", "Mexico"),
    ("Spain", "Spain"),
    ("France", "France"),
    ("Italy", "Italy"),
    ("Germany", "Germany"),
    ("United Kingdom", "United Kingdom"),
    ("Australia", "Australia"),
    ("Japan", "Japan"),
    ("China", "China"),
    ("Brazil", "Brazil"),
    ("Libanon", "Libanon"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.nam
