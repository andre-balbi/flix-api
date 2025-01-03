from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres.models import Genre
import json


@csrf_exempt
def genre_create_list_view(request):
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


@csrf_exempt
def genre_detail_view(request, pk):
    genre = Genre.objects.get(pk=pk)
    data = {"id": genre.id, "name": genre.name}
    return JsonResponse({data})
