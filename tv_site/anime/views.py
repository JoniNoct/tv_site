from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Anime app main page</h1>')


def specific_anime(request, anime_id):
    return HttpResponse(f'<h1>Anime app specific page</h1><p>Anime with {anime_id} id</p>')


