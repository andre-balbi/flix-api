# from genres.views import genre_create_list_view, genre_detail_view
from genres.views import GenreCreateListeView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreate, ReviewRetrieveUpdateDestroy
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("genres/", genre_create_list_view, name="genre-create-list"),
    # path("genres/<int:pk>/", genre_detail_view, name="genre-detail-view"),
    path("genres/", GenreCreateListeView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
    path("actors/", ActorCreateListView.as_view(), name="actors-create-list"),
    path(
        "actors/<int:pk>/",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail-view",
    ),
    path("movies/", MovieCreateListView.as_view(), name="movies-create-list"),
    path(
        "movies/<int:pk>/",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="movies-detail-view",
    ),
    path("reviews/", ReviewListCreate.as_view(), name="review-create-list"),
    path(
        "reviews/<int:pk>/",
        ReviewRetrieveUpdateDestroy.as_view(),
        name="review-detail-view",
    ),
]
