from django.http import JsonResponse
from genres.models import Genre
import json


def genre_view(request):
    if request.method == "GET":
        genres = Genre.objects.all()
        data = [{"id": genre.id, "name": genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        new_genre = Genre(name=data["name"])
        new_genre.save()
        return JsonResponse(
            {"id": new_genre.id, "name": new_genre.name},
            status=201,
        )
