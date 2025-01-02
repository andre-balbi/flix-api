from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    # Sempre que criar uma chave estrangeira, inserir um related_name, para facilitar em consultas futuras
    genre = models.ForeignKey(
        "genres.Genre", on_delete=models.PROTECT, related_name="movies"
    )
    poster = models.CharField(max_length=200, blank=True, null=True)
