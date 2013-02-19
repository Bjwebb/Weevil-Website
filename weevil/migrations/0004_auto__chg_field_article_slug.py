# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.slug'
        db.alter_column(u'weevil_article', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Article.slug'
        db.alter_column(u'weevil_article', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'weevil.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_written'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_illustrated'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            'magazine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weevil.Magazine']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'weevil.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'weevil.magazine': {
            'Meta': {'object_name': 'Magazine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_number': ('django.db.models.fields.IntegerField', [], {}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['weevil']