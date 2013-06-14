# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BaseLibraryItem'
        db.create_table(u'library_baselibraryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal(u'library', ['BaseLibraryItem'])

        # Adding M2M table for field authors on 'BaseLibraryItem'
        m2m_table_name = db.shorten_name(u'library_baselibraryitem_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('baselibraryitem', models.ForeignKey(orm[u'library.baselibraryitem'], null=False)),
            ('author', models.ForeignKey(orm[u'library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['baselibraryitem_id', 'author_id'])

        # Adding model 'Article'
        db.create_table(u'library_article', (
            (u'baselibraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.BaseLibraryItem'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'library', ['Article'])

        # Adding model 'Book'
        db.create_table(u'library_book', (
            (u'baselibraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.BaseLibraryItem'], unique=True, primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'library', ['Book'])

        # Adding model 'Audio'
        db.create_table(u'library_audio', (
            (u'baselibraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.BaseLibraryItem'], unique=True, primary_key=True)),
            ('audio_format', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
        ))
        db.send_create_signal(u'library', ['Audio'])


    def backwards(self, orm):
        # Deleting model 'BaseLibraryItem'
        db.delete_table(u'library_baselibraryitem')

        # Removing M2M table for field authors on 'BaseLibraryItem'
        db.delete_table(db.shorten_name(u'library_baselibraryitem_authors'))

        # Deleting model 'Article'
        db.delete_table(u'library_article')

        # Deleting model 'Book'
        db.delete_table(u'library_book')

        # Deleting model 'Audio'
        db.delete_table(u'library_audio')


    models = {
        u'library.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'library.BaseLibraryItem']},
            u'baselibraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.BaseLibraryItem']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'library.audio': {
            'Meta': {'object_name': 'Audio', '_ormbases': [u'library.BaseLibraryItem']},
            'audio_format': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'baselibraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.BaseLibraryItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library.baselibraryitem': {
            'Meta': {'object_name': 'BaseLibraryItem'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book', '_ormbases': [u'library.BaseLibraryItem']},
            u'baselibraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.BaseLibraryItem']", 'unique': 'True', 'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'library.libraryitem': {
            'Meta': {'object_name': 'LibraryItem'},
            'audio_format': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']