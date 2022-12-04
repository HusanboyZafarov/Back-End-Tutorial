from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("furniture/", views.FurnitureView.as_view(), name='furniture'),
    path("master_class/", views.MasterClassView.as_view(), name='master_class'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("requests/", views.RequestsView.as_view(), name='requests'),
]
