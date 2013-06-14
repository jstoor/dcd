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


#class LibraryItem(models.Model):
#    title = models.CharField(max_length=255)
#    authors = models.ManyToManyField('Author')
#    isbn = models.CharField(max_length=255, blank=True)
#    source = models.CharField(max_length=255, blank=True)
#    audio_format = models.CharField(max_length=4,
#        choices=AUDIO_FORMAT, blank=True)
#    item_type = models.CharField(max_length=4, choices=LIBRARY_ITEM_TYPES)

#    def __unicode__(self):
#        return self.title


class BaseLibraryItem(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    item_type = models.CharField(max_length=4, choices=LIBRARY_ITEM_TYPES)

    def __unicode__(self):
        return self.title

class Book(BaseLibraryItem):
    isbn = models.CharField(max_length=255, blank=True)

class Article(BaseLibraryItem):
    source = models.CharField(max_length=255, blank=True)

class Audio(BaseLibraryItem):
    audio_format = models.CharField(max_length=4,
        choices=AUDIO_FORMAT, blank=True)
