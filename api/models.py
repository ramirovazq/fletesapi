from django.db import models

# Create your models here.

class PhotoReact(models.Model):

    latitud = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    photo_react = models.FileField(upload_to='uploads/', null=True, blank=True,)
    name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

