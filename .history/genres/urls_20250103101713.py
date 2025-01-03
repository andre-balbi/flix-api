from django.urls import path
from genres.views import GenreCreateListeView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("genres/", GenreCreateListeView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
