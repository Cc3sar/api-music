from django.urls import path
from app.music.views import *

urlpatterns = [
    path("api/songs/", SongsList.as_view()),
    path("api/songs/<int:id>/", SongDetails.as_view()),
]