from django.db import models


NATIONALITY_CHOICES = (
    ("US", "United States"),
    ("CA", "Canada"),
    ("MX", "Mexico"),
    ("ES", "Spain"),
    ("FR", "France"),
    ("IT", "Italy"),
    ("DE", "Germany"),
    ("GB", "United Kingdom"),
    ("AU", "Australia"),
    ("JP", "Japan"),
    ("CN", "China"),
    ("BR", "Brazil"),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    natiolanity = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )
