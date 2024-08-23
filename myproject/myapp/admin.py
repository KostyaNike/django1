from django.contrib import admin
from .models import Genre, Game

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'rating')
    filter_horizontal = ('genres',)