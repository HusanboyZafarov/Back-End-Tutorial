from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=150)
    image = models.ImageField(upload_to='Category_Images/%Y-Year/%m-Month')
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("blog:category_detail", kwargs={"slug": self.slug})


class Destination(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True)
    day = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=100)
    image = models.ImageField(upload_to='Destionation_Images/%Y-Year/%m-Month')

    def __str__(self):
        return str(self.title)


class Hotel(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=350, unique=True)
    day = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=100)
    image = models.ImageField(upload_to='Hotels_Images/%Y-Year/%m-Month')

    def __str__(self):
        return str(self.title)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    data_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='Blog_Images/%Y-Year/%m-Month')
    text = models.TextField()
    author_name = models.CharField(max_length=255)
    author_text = models.TextField()
    author_image = models.ImageField(
        upload_to='Author_Images/%y-Year/%m-Month')

    def __str__(self):
        return str(self.title)

    def get_year(self):
        return self.data_time.year

    def get_month(self):
        return self.data_time.month

    def get_day(self):
        return self.data_time.day

    def get_absolute_url(self):
        return reverse("blog:blog_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return str(self.name)
