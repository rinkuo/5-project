from django.shortcuts import render, redirect, get_object_or_404
from .models import Movies

def home(request):
    return render(request, 'home.html')

def movies_list(request):
    movies = Movies.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):  # Updated to accept 'pk' instead of 'id'
    movie = get_object_or_404(Movies, pk=pk)  # Fetch the movie with the given pk
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_form(request):
    if request.method == 'POST':
        title = request.POST['title']
        director = request.POST['director']
        release_year = request.POST['release_year']
        genre = request.POST['genre']
        movie = Movies.objects.create(title=title, director=director, release_year=release_year, genre=genre)
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_form.html')

def movie_update(request, pk):  # Updated to accept 'pk'
    movie = get_object_or_404(Movies, pk=pk)
    if request.method == 'POST':
        movie.title = request.POST['title']
        movie.director = request.POST['director']
        movie.release_year = request.POST['release_year']
        movie.genre = request.POST['genre']
        movie.save()
        return redirect('movies:movie_list')
    return render(request, 'movies/movie_form.html', {'movie': movie})

def movie_delete(request, pk):  # Updated to accept 'pk'
    movie = get_object_or_404(Movies, pk=pk)
    movie.delete()
    return redirect('movies:movie_list')
