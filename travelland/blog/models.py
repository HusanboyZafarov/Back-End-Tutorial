from django.db import models

# Create your models here.


class HappyTraveler(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.name)


class Destination(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    day = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=100)
    image = models.ImageField(upload_to='Destionation_Images/%Y-Year/%M-Month')

    def __str__(self):
        return str(self.title)


class Hotel(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True)
    day = models.PositiveIntegerField(default=5)
    image = models.ImageField(upload_to='Hotels_Images/%Y-Year/%M-Month')

    def __str__(self):
        return str(self.title)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    data_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Blog_Images/%Y-Year/%M-Month')
