from django.urls import path


urlpatterns = [
    path("genres/", views.GenreCreateListeView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
