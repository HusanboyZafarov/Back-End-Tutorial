from django.shortcuts import render, redirect
from .models import Tag, Destination, Hotel, Blog, Comment, Category
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator
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
    page = Paginator(destinations, 6)
    page_number = page.num_pages
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'categories': categories,
        'page': page,
        'page_number': page_number
    }
    return render(request, 'destination.html', context)


def hotels(request):
    categories = Category.objects.all().order_by('-id')
    hotels = Hotel.objects.all().order_by('-id')
    page = Paginator(hotels, 6)
    page_number = page.num_pages
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'categories': categories,
        'page': page,
        'page_number': page_number
    }
    return render(request, 'hotels.html', context)


def blog(request):
    categories = Category.objects.all().order_by('-id')
    blogs = Blog.objects.all().order_by('-id')
    page = Paginator(blogs, 6)
    page_number = page.num_pages
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {
        'categories': categories,
        'page': page,
        'page_number': page_number
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
    context = {
        'categories': categories
    }
    return render(request, 'category.html', context)


def category_detail(request, slug):
    categories = Category.objects.all().order_by('-id')
    category = Category.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=category).order_by('-id')
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


def result(request):
    q = request.GET.get("query")
    if len(q) >= 3:
        query = Blog.objects.filter(
            Q(title__icontains=q)
        )
        context = {
            'blogs': query,
            'query': q,
        }
        return render(request, 'result.html', context)


def search(request):
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {
        'blogs': blogs
    }
    return render(request, 'search.html', context)


def error_404(request, exception):
    return render(request, '404.html')
