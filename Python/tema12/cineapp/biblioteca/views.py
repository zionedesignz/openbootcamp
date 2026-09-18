from django.shortcuts import render
from .models import Genero, Pelicula, Director

# Create your views here.


def index(request):
    num_peliculas = Pelicula.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_peliculas': num_peliculas}
    )
