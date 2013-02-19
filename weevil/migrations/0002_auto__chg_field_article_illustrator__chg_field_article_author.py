# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.illustrator'
        db.alter_column(u'weevil_article', 'illustrator_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['weevil.Contributor']))

        # Changing field 'Article.author'
        db.alter_column(u'weevil_article', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['weevil.Contributor']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Article.illustrator'
        raise RuntimeError("Cannot reverse this migration. 'Article.illustrator' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Article.author'
        raise RuntimeError("Cannot reverse this migration. 'Article.author' and its values cannot be restored.")

    models = {
        u'weevil.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_written'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_illustrated'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            'magazine': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weevil.Magazine']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
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
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['weevil']