from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(unique=True, max_length=155)

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    title = models.CharField(max_length=155)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.PROTECT)
    views = models.PositiveIntegerField(default=0, blank=True)
    image = models.ImageField(upload_to="Post-Images/%Y-Year/%m-Month")
    body = RichTextField()

    def __str__(self):
        return str(self.title)
