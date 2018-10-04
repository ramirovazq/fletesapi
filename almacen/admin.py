# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

class MovimientoAlmacenAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['id_api', 'fecha_creacion', 'fecha_programada', 'picking', 'cantidad', 'producto', 'estado', 'compania', 'propietario', 'detalle']

admin.site.register(MovimientoAlmacen, MovimientoAlmacenAdmin)
