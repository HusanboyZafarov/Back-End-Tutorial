from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Status(models.Model):
    name = models.CharField(max_length=50)
    color_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Statuses"

    def get_absolute_url(self):
        return reverse("note:status_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("note:category_detail", kwargs={"slug": self.slug})


class Notes(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Notes"
