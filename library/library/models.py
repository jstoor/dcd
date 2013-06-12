from django.db import models

LIBRARY_ITEM_TYPES = (
    ('BOOK', 'Book'),
    ('ARTI', 'Article'),
    ('AUDI', 'Audio'),
)

AUDIO_FORMAT = (
    ('CD', 'CD'),
    ('DIGI', 'Digital'),
)

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class LibraryItem(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    item_type = models.CharField(max_length=4, choices=LIBRARY_ITEM_TYPES)

    def __unicode__(self):
        return self.title

class Book(LibraryItem):
    isbn = models.CharField(max_length=255, blank=True)

class Article(LibraryItem):
    source = models.CharField(max_length=255, blank=True)

class Audio(LibraryItem):
    audio_format = models.CharField(max_length=4,
        choices=AUDIO_FORMAT, blank=True)