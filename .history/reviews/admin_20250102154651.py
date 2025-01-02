from django.contrib import admin
from reviews.models import Review


class ReviewAdmin(Review):
    list_display = ("id", "movie", "stars")


# Register your models here.
