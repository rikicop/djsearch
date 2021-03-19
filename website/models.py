from django.db import models

class Inmueble(models.Model):
    codigo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=1000)
    edo = models.CharField(max_length=1000,blank=True)
    precio = models.DecimalField(max_digits=7,decimal_places=2)
    #imagen = models.CharField(max_length=1000)

    def __str__(self):
        template = '{0.codigo} {0.tipo} {0.ubicacion} {0.edo} {0.precio}'
        return template.format(self)
