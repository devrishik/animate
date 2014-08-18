# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Frame'
        db.create_table(u'pages_frame', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('appStoreLink', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('width', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'pages', ['Frame'])


    def backwards(self, orm):
        # Deleting model 'Frame'
        db.delete_table(u'pages_frame')


    models = {
        u'pages.frame': {
            'Meta': {'object_name': 'Frame'},
            'appStoreLink': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['pages']