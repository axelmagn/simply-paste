# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Snippet'
        db.create_table(u'snippets_snippet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.CharField')(default='text', max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'snippets', ['Snippet'])


    def backwards(self, orm):
        # Deleting model 'Snippet'
        db.delete_table(u'snippets_snippet')


    models = {
        u'snippets.snippet': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Snippet'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '100'})
        }
    }

    complete_apps = ['snippets']