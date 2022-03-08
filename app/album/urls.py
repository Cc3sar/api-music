from django.urls import path
from app.album.views import *

urlpatterns = [
    path("api/albums/", AlbumsList.as_view()),
    path("api/albums/<int:id>/", AlbumDetails.as_view()),
]