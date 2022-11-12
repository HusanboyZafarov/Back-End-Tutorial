from django.shortcuts import render, redirect
from .models import Tag, Destination, Hotel, Blog, Comment, Category
from .forms import CommentForm
from django.db.models import Count
# Create your views here.


def home(request):
    destinations = Destination.objects.all().order_by('-id')[:4]
    hotels = Hotel.objects.all().order_by('-id')[:3]
    blogs = Blog.objects.all().order_by('-id')[:3]
    categories = Category.objects.all().order_by('-id')
    context = {
        'destinations': destinations,
        'hotels': hotels,
        'blogs': blogs,
        'categories': categories,
    }
    return render(request, 'index.html', context)


def about(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
    }
    return render(request, 'about.html', context)


def destination(request):
    categories = Category.objects.all().order_by('-id')
    destinations = Destination.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'destinations': destinations
    }
    return render(request, 'destination.html', context)


def hotels(request):
    categories = Category.objects.all().order_by('-id')
    hotels = Hotel.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'hotels': hotels
    }
    return render(request, 'hotels.html', context)


def blog(request):
    categories = Category.objects.all().order_by('-id')
    blogs = Blog.objects.all().order_by('-id')
    context = {
        'categories': categories,
        'blogs': blogs
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    categories = Category.objects.all().order_by('-id')
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
        'categories': categories,
        'form': form
    }
    return render(request, 'blog-single.html', context)


def category(request):
    categories = Category.objects.all().order_by('-id')
    categories_list = Category.objects.annotate(posts_count=Count('blog'))
    print(categories_list.values())
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


def category_detail(request, slug):
    categories = Category.objects.all().order_by('-id')
    category = Category.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=category)
    context = {
        'blogs': blogs,
        'object': category,
        'categories': categories,
    }
    return render(request, 'category_detail.html', context)


def contact(request):
    categories = Category.objects.all().order_by('-id')
    context = {
        'categories': categories,
    }
    return render(request, 'contact.html', context)
