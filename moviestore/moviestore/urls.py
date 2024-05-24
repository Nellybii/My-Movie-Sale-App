
from django.contrib import admin
from django.urls import path, include
from movies.views.user_View import createUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/user/register/', createUserView.as_view(), name='register'),
     path("movies/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("movies/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("movies-auth/", include("rest_framework.urls")),
    path("movies/", include("movies.urls"))
]
