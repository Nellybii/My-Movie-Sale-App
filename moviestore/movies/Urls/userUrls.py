from django.urls import path
from ..views.user_View import register_user, login_user

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register_user, name='register'),
]