from django.contrib import admin
from django.db import models
from .models import Author, LibraryItem


class LibraryItemAdmin(admin.ModelAdmin):
    model = LibraryItem


class AuthorAdmin(admin.ModelAdmin):
    model = Author


admin.site.register(LibraryItem, LibraryItemAdmin)
admin.site.register(Author, AuthorAdmin)
