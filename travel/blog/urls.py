from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('hotels/', views.hotels, name='hotels'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category_detail/<slug:slug>/',
         views.category_detail, name='category_detail'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('result_page/', views.result, name='result'),
]
