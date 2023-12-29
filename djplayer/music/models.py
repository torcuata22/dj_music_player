from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    album_image=models.FileField(upload_to="images")

    def __str__(self):
        return self.album_name
    
class Song(models.Model):
    song_name = models.CharField(max_length=50, default="name")
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs_in_album')
    song_file = models.FileField(upload_to='songs')
    picture = models.FileField(upload_to='picture')
    artist_name = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs_by_artist', default='Artist')

    def __str__(self):
        return f"{self.song_name} - {self.artist_name}"