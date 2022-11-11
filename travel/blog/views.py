from django.shortcuts import render, redirect
from .models import Tag, Destination, Hotel, Blog, Comment, Category
from .forms import CommentForm
# Create your views here.


def home(request):
    destinations = Destination.objects.all().order_by('-id')[:4]
    hotels = Hotel.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {
        'destinations': destinations,
        'hotels': hotels,
        'blogs': blogs
    }
    return render(request, 'index.html', context)


def about(request):
    context = {

    }
    return render(request, 'about.html', context)


def destination(request):
    destinations = Destination.objects.all().order_by('-id')
    context = {
        'destinations': destinations
    }
    return render(request, 'destination.html', context)


def hotels(request):
    hotels = Hotel.objects.all().order_by('-id')
    context = {
        'hotels': hotels
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
    categories = Category.objects.all()
    comments = Comment.objects.filter(blog=blog).order_by('-id')
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.blog = blog
            instance.save()
            return redirect(f'/blog_detail/{slug}')
    else:
        form = CommentForm()
    context = {
        'blogs': blogs,
        'blog': blog,
        'tags': tags,
        'categories': categories,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog-single.html', context)


def contact(request):
    context = {

    }
    return render(request, 'contact.html', context)
