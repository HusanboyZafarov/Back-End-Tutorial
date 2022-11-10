from django.shortcuts import render
from .models import Tag, HappyTraveler, Destination, Hotel, Blog, Comment, Category
# Create your views here.


def home(request):
    destinations = Destination.objects.all().order_by('-id')[:4]
    hotels = Hotel.objects.all().order_by('-id')[:3]
    context = {
        'destinations': destinations,
        'hotels': hotels,
    }
    return render(request, 'index.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)


def destination(request):
    context = {

    }
    return render(request, 'destination.html', context)


def hotels(request):
    context = {

    }
    return render(request, 'hotels.html', context)


def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    blogs = Blog.objects.all().order_by('-id')[:3]
    tags = Tag.objects.all().order_by('id')
    context = {
        'blogs': blogs,
        'blog': blog,
        'tags': tags
    }
    return render(request, 'blog-single.html', context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)
