# -*- coding: utf-8 -*-

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class PhotoReact(models.Model):

    latitud = models.DecimalField(max_digits=12, decimal_places=9, default=0)
    longitud = models.DecimalField(max_digits=12, decimal_places=9, default=0)
    photo_react = models.ImageField(upload_to='uploads/', null=True, blank=True,)
    photo_thumbnail = ImageSpecField(source='photo_react',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
    name = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def photo_react_thumbnail_url(self):
      answer= ""
      if self.photo_thumbnail:
        answer = self.photo_thumbnail.name
      return answer

    def __str__(self):
      return '%s %s' % (self.id, self.name)