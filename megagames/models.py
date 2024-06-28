
from django.db import models

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.TextField("Descripción")
    precio = models.IntegerField("Precio")
    consolas = models.CharField("Consolas", max_length=100)
    stock = models.IntegerField("Stock")
    url_imagen = models.URLField("URL de la Imagen", max_length=200)

    def __str__(self):
        return self.nombre


class Consola(models.Model):
    idconsola = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=100)
    url_imagen = models.URLField("URL de la Imagen", max_length=200)
    stock = models.IntegerField("Stock")
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.nombre