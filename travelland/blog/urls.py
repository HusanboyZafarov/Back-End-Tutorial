from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('hotels/', views.hotels, name='hotels'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
