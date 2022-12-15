from django.contrib import admin
from .models import Category, Post
# Register your models here.


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post)
