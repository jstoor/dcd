# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'library_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'library', ['Author'])

        # Adding model 'LibraryItem'
        db.create_table(u'library_libraryitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('isbn', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('audio_format', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('item_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
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


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'library_author')

        # Deleting model 'LibraryItem'
        db.delete_table(u'library_libraryitem')

        # Removing M2M table for field authors on 'LibraryItem'
        db.delete_table(db.shorten_name(u'library_libraryitem_authors'))


    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'library.libraryitem': {
            'Meta': {'object_name': 'LibraryItem'},
            'audio_format': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'item_type': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['library']