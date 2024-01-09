from django.urls import path
from .views import song_list, song_detail, home, add_artist, add_song

urlpatterns = [
    path('', home, name='home'),
    path('songs/', song_list, name='song_list'),
    path('songs/<int:pk>/', song_detail, name='song_detail'),
    
    path('add_song/', add_song, name='add_song'),
    path('add_artist/', add_artist, name='add_artist'),
]
