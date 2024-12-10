from django.db import models
from django.urls import reverse

class Music(models.Model):
    album_title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('music:music_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('music:music_update', args=[self.pk])

    def get_delete_url(self):
        return reverse('music:music_delete', args=[self.pk])

    def __str__(self):
        return self.album_title
