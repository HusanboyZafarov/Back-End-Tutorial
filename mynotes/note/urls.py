from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path("", views.NotesView.as_view(), name='home'),
    path("add/", views.AddNoteView.as_view(), name='add'),
    path("category_detail/<slug:slug>",
         views.category_detail, name='category_detail'),
    path("status_detail/<slug:slug>",
         views.status_detail, name='status_detail'),
]
