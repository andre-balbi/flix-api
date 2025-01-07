from reviews.models import Review
from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from django.http import JsonResponse
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieStatsSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse(
                {"detail": "❌ Movie deleted successfully!"}, status=204
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        # como se fosse group_by do sql (group by genre_name)
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )
        total_reviews = Review.objects.count()
        average_total_stars = Review.objects.aggregate(Avg("stars"))["stars__avg"]

        movie_stats = {
            "total_movies": total_movies,
            "movies_by_genre": movies_by_genre,
            "total_reviews": total_reviews,
            "average_total_stars": (
                round(average_total_stars, 2) if average_total_stars else 0
            ),
        }
        serializer = MovieStatsSerializer(data=movie_stats)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
