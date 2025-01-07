from rest_framework import generics

# , exceptions
from django.http import JsonResponse
from genres.models import Genre
from genres.serializers import GenreSerializer

from rest_framework.permissions import IsAuthenticated

# from genres.permissions import GenrePermissionClass
from app.permissions import GlobalDefaultPermission


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# import json


class GenreCreateListeView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        # GenrePermissionClass,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    # def handle_exception(self, exc):
    # if isinstance(exc, exceptions.NotAuthenticated):
    #     return JsonResponse({"detail": "acesso negado"}, status=403)
    # return super().handle_exception(exc)


# class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Genre.objects.all()
#     serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        # GenrePermissionClass,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse(
                {"detail": "❌ Genre deleted successfully!"}, status=204
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == "GET":
#         genres = Genre.objects.all()
#         data = [{"id": genre.id, "name": genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     elif request.method == "POST":
#         data = json.loads(request.body.decode("utf-8"))
#         new_genre = Genre(name=data["name"])
#         new_genre.save()
#         return JsonResponse(
#             {"id": new_genre.id, "name": new_genre.name},
#             status=201,
#         )

# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
#     if request.method == "GET":
#         data = {"id": genre.id, "name": genre.name}
#         return JsonResponse(data)

#     elif request.method == "PUT":
#         data = json.loads(request.body.decode("utf-8"))
#         genre.name = data["name"]
#         genre.save()
#         return JsonResponse({"id": genre.id, "name": genre.name})

#     elif request.method == "DELETE":
#         genre.delete()
#         return JsonResponse({"message": "Genre deleted successfully"}, status=204)
