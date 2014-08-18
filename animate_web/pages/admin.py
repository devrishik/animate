# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, unicode_literals

from django.contrib import admin

from .models import Frame

#==============================================================================
# ADMIN MODELS
#==============================================================================


class FrameAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover_image', 'video')

#==============================================================================
# REGISTER MODELS
#==============================================================================
admin.site.register(Frame, FrameAdmin)
