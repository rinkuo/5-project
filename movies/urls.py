from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies_list, name='movie_list'),  # This should be named 'movie_list'
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/new/', views.movie_form, name='movie_create'),
    path('movie/<int:pk>/edit/', views.movie_update, name='movie_update'),  # Updated to use 'pk'
    path('movie/<int:pk>/delete/', views.movie_delete, name='movie_delete'),  # Updated to use 'pk'
]
