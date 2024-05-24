from django.urls import path
from movies.views.user_View import createUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('login', createUserView, name='login'),
    path('register', createUserView, name='register'),
]