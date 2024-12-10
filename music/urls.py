from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.music_list, name='music_list'),
    path('music/<int:pk>/', views.music_detail, name='music_detail'),
    path('music/new/', views.music_form, name='music_create'),
    path('music/<int:pk>/edit/', views.music_update, name='music_update'),  # Use music_update here
    path('music/<int:pk>/delete/', views.music_delete, name='music_delete'),
]
