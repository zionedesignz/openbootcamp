from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='ID único')
    titulo = models.CharField(max_length=255, help_text='Ingrese el título.')
    año = models.IntegerField(help_text='Ingrese el año de lanzamiento.')
    imagen = models.CharField(
        max_length=255, help_text='Ingrese la url de la potada.')
    director = models.ForeignKey(
        'Director', on_delete=models.SET_NULL, null=True)
    genero = models.ManyToManyField(Genero)
    descripcion = models.CharField(
        max_length=100, help_text='Ingrese una breve despcripción.')

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('pelicula-detalle', args=[str(self.id)])


class Director(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='ID único')
    nombre = models.CharField(
        max_length=100, help_text='Ingrese el nombre del director.')
    apellidos = models.CharField(
        max_length=100, help_text='Ingrese los apellidos del director.')
    imagen = models.CharField(
        max_length=255, help_text='Ingrese la url de una imagen del director.')

    def __str__(self):
        return '%s, %s' % (self.apellidos, self.nombre)

    def get_absolute_url(self):
        return reverse('director-detalle', args=[str(self.id)])