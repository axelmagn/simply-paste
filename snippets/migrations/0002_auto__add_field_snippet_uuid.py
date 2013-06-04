# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Snippet.uuid'
        db.add_column(u'snippets_snippet', 'uuid',
                      self.gf('shortuuidfield.fields.ShortUUIDField')(default='', max_length=22, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Snippet.uuid'
        db.delete_column(u'snippets_snippet', 'uuid')


    models = {
        u'snippets.snippet': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Snippet'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '100'}),
            'uuid': ('shortuuidfield.fields.ShortUUIDField', [], {'max_length': '22', 'blank': 'True'})
        }
    }

    complete_apps = ['snippets']