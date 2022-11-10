from django.shortcuts import render
from .models import Tag, HappyTraveler, Destination, Hotel, Blog, Comment
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
    context = {

    }
    return render(request, 'blog.html', context)


def blog_detail(request):
    context = {

    }
    return render(request, 'blog.html', context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)
