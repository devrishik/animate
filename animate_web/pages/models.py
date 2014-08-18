# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from .utils import get_upload_file_path, get_video_upload_file_path

# Create your models here, but defer to having them in their own app if possible.

class Frame(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    appStoreLink = models.CharField(_("App Store Link"), max_length=500)
    description = models.CharField(_("Description"), max_length=500)

    cover_image = models.ImageField(_('Cover Image'),
                                    upload_to=get_upload_file_path,
                                    height_field='height',
                                    width_field='width')
    width = models.IntegerField(_("width"), blank=True, editable=False)
    height = models.IntegerField(_("Height"), blank=True, editable=False)
    
    video = models.FileField(upload_to=get_video_upload_file_path)

    def __unicode__(self):
    	return self.name
