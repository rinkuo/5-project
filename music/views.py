from django.shortcuts import render, redirect, get_object_or_404
from .models import Music

def music_list(request):
    music = Music.objects.all()
    ctx = {'music': music}
    return render(request, 'music/music_list.html', ctx)

def music_detail(request, pk):
    music = get_object_or_404(Music, pk=pk)
    ctx = {'music': music}
    return render(request, 'music/music_detail.html', ctx)

def music_form(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        release_date = request.POST.get('release_date')
        genre = request.POST.get('genre')
        if album_title and artist and release_date and genre:
            Music.objects.create(
                album_title=album_title,
                artist=artist,
                release_date=release_date,
                genre=genre,
            )
            return redirect('music:music_list')
    return render(request, 'music/music_form.html')

def music_update(request, pk):
    music = get_object_or_404(Music, pk=pk)
    if request.method == 'POST':
        music.album_title = request.POST.get('album_title')
        music.artist = request.POST.get('artist')
        music.release_date = request.POST.get('release_date')
        music.genre = request.POST.get('genre')
        music.save()
        return redirect(music.get_detail_url())

    ctx = {'music': music}
    return render(request, 'music/music_form.html', ctx)

def music_delete(request, pk):
    music = get_object_or_404(Music, pk=pk)
    music.delete()
    return redirect('music:music_list')
