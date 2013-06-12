from django.contrib import admin
from django.db import models
from .models import Author, LibraryItem


class BookAdmin(admin.ModelAdmin):
    model = Book

class ArticleAdmin(admin.ModelAdmin):
    model = Article

class AudioAdmin(admin.ModelAdmin):
    model = Audio

class AuthorAdmin(admin.ModelAdmin):
    model = Author



admin.site.register(Book, BookAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Audio, AudioAdmin)
admin.site.register(Author, AuthorAdmin)





