from django.shortcuts import render

# Create your views here.


def home(request):
    context = {

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


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)
