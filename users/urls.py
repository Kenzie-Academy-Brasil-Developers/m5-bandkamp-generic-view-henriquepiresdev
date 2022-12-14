from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("users/", views.CreateUserView.as_view()),
    path("users/<int:pk>/", views.RetrieveUpdateDestroyMovieView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
    path("docs/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
