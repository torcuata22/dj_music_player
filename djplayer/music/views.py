from django.shortcuts import render
from .models import Album, Song

# Create your views here.

def home(request):
    albums = Album.objects.all()
    return render(request, 'music/home.html', {'albums':albums})