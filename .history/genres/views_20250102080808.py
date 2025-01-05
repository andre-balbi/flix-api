from django.http import JsonResponse


def genre_view(request):
    return Response({"message": "API de g neros"})
