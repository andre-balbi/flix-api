# from genres.views import genre_create_list_view, genre_detail_view
# from genres.views import GenreCreateListeView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewListCreate, ReviewRetrieveUpdateDestroy
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("genres/", genre_create_list_view, name="genre-create-list"),
    # path("genres/<int:pk>/", genre_detail_view, name="genre-detail-view"),
    # path("genres/", GenreCreateListeView.as_view(), name="genre-create-list"),
    # path(
    #     "genres/<int:pk>/",
    #     GenreRetrieveUpdateDestroyView.as_view(),
    #     name="genre-detail-view",
    # ),
    #
    # The lines above is including the urls.py file from the genres app.
    # The "api/v1/" part is a prefix that will be added to all the URLs
    # that are defined in the genres/urls.py file. For example, if the
    # genres/urls.py file defines a URL like path("genres/", ...), then
    # the final URL will be path("api/v1/genres/", ...). This is a common
    # pattern in Django projects, where different apps define their own
    # URLs and then include them in the main project's urls.py file.
    # This helps to keep the code organized and makes it easier to manage
    # the URLs in a large project.
    path("api/v1/", include("genres.urls")),
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
