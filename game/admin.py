from django.contrib import admin
from .models import *


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_release', 'time_create',
                    'cat', 'image', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, GameAdmin)
admin.site.register(Category, CategoryAdmin)
