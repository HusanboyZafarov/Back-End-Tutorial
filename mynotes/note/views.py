from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.
from .models import Notes, Category, Status
from .forms import AddNoteForm


class NotesView(ListView):
    """all notes view"""
    model = Notes
    paginate_by = 10


class AddNoteView(View):
    """One note view"""
    template_name = 'note/add.html'

    def get(self, request, *args, **kwargs):
        form = AddNoteForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            form = AddNoteForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/")
        else:
            render(request, self.template_name)
        return render(request, self.template_name, {"form": form})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    notes = Notes.objects.filter(category=category)
    context = {
        'category': category,
        'notes': notes
    }
    return render(request, 'note/category_notes.html', context)


def status_detail(request, slug):
    status = Status.objects.get(slug=slug)
    notes = Notes.objects.filter(status=status)
    context = {
        'status': status,
        'notes': notes
    }
    return render(request, 'note/status.html', context)
