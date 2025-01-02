from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView

from django.contrib import admin
from django.urls import path

# from genres.views import genre_create_list_view, genre_detail_view
from genres.views import GenreCreateListeView, GenreRetrieveUpdateDestroyView


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
]
