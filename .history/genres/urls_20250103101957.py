from django.urls import path
from . import views  # Import all view functions from the views.py file


urlpatterns = [
    path("genres/", views.GenreCreateListeView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
