# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        #import random, sha, string

        from library.models import LIBRARY_ITEM_TYPES

        for old_library_item in orm.LibraryItem.objects.all():
            new_item = None

            #BOOK
            if old_library_item.item_type == LIBRARY_ITEM_TYPES[0][0]: 
                new_item = orm.Book.objects.create()
                new_item.isbn = old_library_item.isbn
            #ARTI
            elif old_library_item.item_type == LIBRARY_ITEM_TYPES[1][0]: 
                new_item = orm.Article.objects.create()
                new_item.source = old_library_item.source
            #AUDI
            elif old_library_item.item_type == LIBRARY_ITEM_TYPES[2][0]: 
                new_item = orm.Audio.objects.create()
                new_item.audio_format = old_library_item.audio_format

            if new_item:
                new_item.item_type = old_library_item.item_type
                new_item.title = old_library_item.title
                new_item.authors = old_library_item.authors
                new_item.save()



    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

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
    symmetrical = True
