# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Snippet.id'
        db.delete_column(u'snippets_snippet', u'id')


        # Changing field 'Snippet.uuid'
        db.alter_column(u'snippets_snippet', 'uuid', self.gf('shortuuidfield.fields.ShortUUIDField')(unique=True, max_length=22, primary_key=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Snippet.id'
        raise RuntimeError("Cannot reverse this migration. 'Snippet.id' and its values cannot be restored.")

        # Changing field 'Snippet.uuid'
        db.alter_column(u'snippets_snippet', 'uuid', self.gf('shortuuidfield.fields.ShortUUIDField')(max_length=22, unique=True))

    models = {
        u'snippets.snippet': {
            'Meta': {'ordering': "('created',)", 'object_name': 'Snippet'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '100'}),
            'uuid': ('shortuuidfield.fields.ShortUUIDField', [], {'unique': 'True', 'max_length': '22', 'primary_key': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['snippets']