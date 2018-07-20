# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class PhotoReactAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields  = ['id', 'name']
    list_display = ['id', 'name', 'photo_react', 'latitud', 'longitud']

class LimeDemoAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields  = ['id', 'name', 'email']
    list_display = ['id', 'name', 'email', 'api_consulting', 'created', 'updated', 'token']


admin.site.register(PhotoReact, PhotoReactAdmin)
admin.site.register(LimeDemo, LimeDemoAdmin)
# Register your models here.

