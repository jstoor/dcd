# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'library_book', (
            (u'libraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.LibraryItem'], unique=True, primary_key=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'library', ['Book'])

        # Adding model 'Audio'
        db.create_table(u'library_audio', (
            (u'libraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.LibraryItem'], unique=True, primary_key=True)),
            ('audio_format', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
        ))
        db.send_create_signal(u'library', ['Audio'])

        # Adding model 'Article'
        db.create_table(u'library_article', (
            (u'libraryitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['library.LibraryItem'], unique=True, primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'library', ['Article'])

        # Deleting field 'LibraryItem.audio_format'
        db.delete_column(u'library_libraryitem', 'audio_format')

        # Deleting field 'LibraryItem.source'
        db.delete_column(u'library_libraryitem', 'source')

        # Deleting field 'LibraryItem.isbn'
        db.delete_column(u'library_libraryitem', 'isbn')


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'library_book')

        # Deleting model 'Audio'
        db.delete_table(u'library_audio')

        # Deleting model 'Article'
        db.delete_table(u'library_article')

        # Adding field 'LibraryItem.audio_format'
        db.add_column(u'library_libraryitem', 'audio_format',
                      self.gf('django.db.models.fields.CharField')(default='DIGI', max_length=4),
                      keep_default=False)

        # Adding field 'LibraryItem.source'
        db.add_column(u'library_libraryitem', 'source',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255),
                      keep_default=False)

        # Adding field 'LibraryItem.isbn'
        db.add_column(u'library_libraryitem', 'isbn',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=255),
                      keep_default=False)


    models = {
        u'library.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'library.LibraryItem']},
            u'libraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.LibraryItem']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'library.audio': {
            'Meta': {'object_name': 'Audio', '_ormbases': [u'library.LibraryItem']},
            'audio_format': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            u'libraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.LibraryItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book', '_ormbases': [u'library.LibraryItem']},
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'libraryitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['library.LibraryItem']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.libraryitem': {
            'Meta': {'object_name': 'LibraryItem'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']