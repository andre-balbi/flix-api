from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [  # URLs for the authentication app
    path(
        "authentication/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
]
