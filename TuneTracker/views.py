# from django.shortcuts import render, redirect
# from .models import Song

# def song_list(request):
#     songs = Song.objects.all()
#     return render(request, 'TuneTracker/song_list.html', {'songs': songs})

# def song_detail(request, pk):
#     song = Song.objects.get(pk=pk)
#     return render(request, 'TuneTracker/song_detail.html', {'song': song})


# TuneTracker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Song, Artist
from .forms import SongForm, ArtistForm
def home(request):
    return redirect('song_list')

 

def song_list(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()

    context = {'songs': songs, 'artists': artists}
    return render(request, 'TuneTracker/song_list.html', context)




def song_detail(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'TuneTracker/song_detail.html', {'song': song})

 
def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            new_song = form.save(commit=False)
            new_song.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'TuneTracker/add_song.html', {'form': form})

 
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            new_artist = form.save(commit=False)
            new_artist.save()
            return redirect('song_list')  
    else:
        form = ArtistForm()
    return render(request, 'TuneTracker/add_artist.html', {'form': form})
