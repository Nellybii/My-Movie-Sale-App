from django.urls import path
from movies.views.movieView import MovieList, MovieUpdate,MovieCreate
from movies.views.directorView import DirectorList, DirectorCreate, DirectorUpdate
from movies.views.genreView import GenreCreate, GenreList, GenreUpdate
from movies.views.ReviewView import ReviewList, ReviewUpdate, ReviewCreate

urlpatterns = [
    path('list/', MovieList.as_view(), name='movie_list'),
    path('create/', MovieCreate.as_view(), name='create_movie'),
    path('<int:pk>/', MovieUpdate.as_view(), name='update_movie'),  

    path('directors/', DirectorList.as_view(), name='director-list'),
    path('directors/create/', DirectorCreate.as_view(), name='director-create'),
    path('directors/<int:pk>/', DirectorUpdate.as_view(), name='director-update-delete'),

    path('genres/', GenreList.as_view(), name='genre-list'),
    path('genres/create/', GenreCreate.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreUpdate.as_view(), name='genre-update-delete'),

    path('reviews/', ReviewList.as_view(), name='reviews-list'),
    path('reviews/create/', ReviewCreate.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewUpdate.as_view(), name='review-update-delete'),
]