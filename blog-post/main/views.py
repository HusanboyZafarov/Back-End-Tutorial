from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Post


class PostsView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class BookDetailView(DetailView):
    model = Post


class CategoryListView(ListView):
    model = Category
    template_name = 'main/category_list.html'

    def get_queryset(self):
        if self.kwargs.get('slug'):
            category = self.model.objects.get(slug=self.kwargs.get('slug'))
            queryset = Post.objects.filter(category=category)
        return queryset


class CreatePostView(CreateView):
    model = Post
    fields = ["title", "category", "image", "body"]
    success_url = "/"


class UpdatePostView(UpdateView):
    template_name = 'main/book_form.html'
    model = Post
    fields = ["title", "category", "image", "body"]
    success_url = "/"
    


class DeletePostView(DeleteView):
    model = Post
    success_url = "/"
