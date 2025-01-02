from django.http import JsonResponse
from genres.models import Genre


def genre_view(request):
    genres = Genre.objects.all()
    return JsonResponse({genres})
