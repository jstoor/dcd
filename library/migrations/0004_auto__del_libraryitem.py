# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LibraryItem'
        db.delete_table(u'library_libraryitem')

        # Removing M2M table for field authors on 'LibraryItem'
        db.delete_table(db.shorten_name(u'library_libraryitem_authors'))


    def backwards(self, orm):
        # Adding model 'LibraryItem'
        db.create_table(u'library_libraryitem', (
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('audio_format', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'library', ['LibraryItem'])

        # Adding M2M table for field authors on 'LibraryItem'
        m2m_table_name = db.shorten_name(u'library_libraryitem_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('libraryitem', models.ForeignKey(orm[u'library.libraryitem'], null=False)),
            ('author', models.ForeignKey(orm[u'library.author'], null=False))
        ))
        db.create_unique(m2m_table_name, ['libraryitem_id', 'author_id'])


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
        }
    }

    complete_apps = ['library']