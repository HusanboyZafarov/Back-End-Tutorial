from django.contrib import admin
from .models import Destination, Hotel, Blog, Comment, Tag, Category
# Register your models here.


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Category)
class AdminTag(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Destination)
class AdminDestination(admin.ModelAdmin):
    list_display = ['title', 'price', 'day', 'id']
    list_display_links = ['title', 'price', 'day', 'id']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Hotel)
class AdminHotel(admin.ModelAdmin):
    list_display = ['title', 'price', 'day', 'id']
    list_display_links = ['title', 'price', 'day', 'id']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title', 'category', 'data_time', 'author_name', 'id']
    list_display_links = ['title', 'category',
                          'data_time', 'author_name', 'id']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title__name']


admin.site.register(Comment)
