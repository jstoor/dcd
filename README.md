# Info
This is a small Django project which has no views, no templates and no functionality beyond the inclusion of a couple of models.

The two models, Author and LibraryItem represent a set of items available in a library. The 'type' field on LibraryItem represents the physical category of item in to which the item falls. There are attributes on the LibraryItem that only apply to a subset of the 'types'.

There is an SQLite3 database in library/sqlite.db which contains a few example items.

You will need Git, Django 1.5.1 and South 0.8.1 to complete the below tasks.

Complete as many of the tasks below as possible, archive the directory (including the .git directory) and return by e-mail.

# Tasks
 1. Initialise a Git repository in this directory, commit your changes as you go.
 2. Change the LibraryItem model in to three separate models (Use model inheritance where applicable to reduce duplication):
    - Book; with title, authors & ISBN fields
    - Article; with title, authors & source fields
    - Audio; with title, authors & audio format fields.
 3. Use South to generate/create both schema migrations and data migrations to bring the included database up to the new schema while maintaining the existing data. You only need to provide a forward migration for the data, reverse can be ignored.
 4. Run the migrations on the provided database.