# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.order'
        db.add_column(u'weevil_article', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'Article.magazine'
        db.alter_column(u'weevil_article', 'magazine_id', self.gf('adminsortable.fields.SortableForeignKey')(to=orm['weevil.Magazine']))
        # Adding field 'Magazine.order'
        db.add_column(u'weevil_magazine', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.order'
        db.delete_column(u'weevil_article', 'order')


        # Changing field 'Article.magazine'
        db.alter_column(u'weevil_article', 'magazine_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weevil.Magazine']))
        # Deleting field 'Magazine.order'
        db.delete_column(u'weevil_magazine', 'order')


    models = {
        u'weevil.article': {
            'Meta': {'ordering': "['order']", 'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_written'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'articles_illustrated'", 'null': 'True', 'to': u"orm['weevil.Contributor']"}),
            'magazine': ('adminsortable.fields.SortableForeignKey', [], {'to': u"orm['weevil.Magazine']"}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'weevil.committee': {
            'Meta': {'object_name': 'Committee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'weevil.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'weevil.magazine': {
            'Meta': {'ordering': "['order']", 'object_name': 'Magazine'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue_number': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'weevil.news': {
            'Meta': {'object_name': 'News'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['weevil']