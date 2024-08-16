from django.urls import path 
from .views import blog_list, blog_details

urlpatterns = [
    path('list/',blog_list,name='blog-list'),
    path('<slug:slug>/',blog_details,name='blog-details'),


]