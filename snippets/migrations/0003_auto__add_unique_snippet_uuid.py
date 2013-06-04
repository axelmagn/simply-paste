# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Snippet', fields ['uuid']
        db.create_index(u'snippets_snippet', ['uuid'])

        # Adding unique constraint on 'Snippet', fields ['uuid']
        db.create_unique(u'snippets_snippet', ['uuid'])


    def backwards(self, orm):
        # Removing unique constraint on 'Snippet', fields ['uuid']
        db.delete_unique(u'snippets_snippet', ['uuid'])

        # Removing index on 'Snippet', fields ['uuid']
        db.delete_index(u'snippets_snippet', ['uuid'])


    models = {
        u'snippets.snippet': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Snippet'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '100'}),
            'uuid': ('shortuuidfield.fields.ShortUUIDField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '22', 'blank': 'True'})
        }
    }

    complete_apps = ['snippets']