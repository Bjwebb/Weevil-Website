# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Magazine'
        db.create_table(u'weevil_magazine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue_number', self.gf('django.db.models.fields.IntegerField')()),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'weevil', ['Magazine'])

        # Adding model 'Contributor'
        db.create_table(u'weevil_contributor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'weevil', ['Contributor'])

        # Adding model 'Article'
        db.create_table(u'weevil_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_written', to=orm['weevil.Contributor'])),
            ('illustrator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles_illustrated', to=orm['weevil.Contributor'])),
            ('magazine', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weevil.Magazine'])),
        ))
        db.send_create_signal(u'weevil', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Magazine'
        db.delete_table(u'weevil_magazine')

        # Deleting model 'Contributor'
        db.delete_table(u'weevil_contributor')

        # Deleting model 'Article'
        db.delete_table(u'weevil_article')


    models = {
        u'weevil.article': {
            'Meta': {'object_name': 'Article'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_written'", 'to': u"orm['weevil.Contributor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illustrator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles_illustrated'", 'to': u"orm['weevil.Contributor']"}),
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