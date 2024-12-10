from django.contrib import admin
from django.urls import path, include
from movies.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('movies/', include('movies.urls')),
    path('sports/', include('sports.urls')),
    path('music/', include('music.urls')),
    path('travel/', include('travel.urls')),
]
