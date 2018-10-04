from django.db import models

# Create your models here.
class MovimientoAlmacen(models.Model):
    id_api = models.IntegerField()
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_programada = models.DateTimeField(blank=True, null=True)
    fecha_hecho = models.DateTimeField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)
    picking = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )
    cantidad = models.SmallIntegerField(default=0)
    producto = models.CharField(
        max_length=300,
        null=True,
        blank=True
        )
    de = models.CharField(
        max_length=300,
        null=True,
        blank=True
        )
    para = models.CharField(
        max_length=300,
        null=True,
        blank=True
        )
    estado =  models.CharField(
        max_length=50,
        null=True,
        blank=True
        )
    compania = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    propietario = models.CharField(
        max_length=200,
        null=True,
        blank=True
        )

    detalle = models.CharField(
        max_length=200,
        null=True,
        blank=True
        )


    def __str__(self):
        return u"%s (%s) %s %s" % (self.id, self.id_api, self.producto, self.cantidad)
