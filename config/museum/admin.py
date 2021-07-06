from django.contrib import admin

from .models import Author, Picture


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'born', 'die')


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
