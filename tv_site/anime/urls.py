from django.urls import path

from .views import index, specific_anime

urlpatterns = [
    path('', index),
    path('<int:anime_id>', specific_anime),
]