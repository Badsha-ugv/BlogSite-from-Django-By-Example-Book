from django.urls import path 
from .views import blog_list, blog_details, share_post



urlpatterns = [
    path('list/',blog_list,name='blog-list'),
    path('list/<slug:tag_slug>/',blog_list,name='blog_list_by_tag'),
    path('<slug:slug>/',blog_details,name='blog-details'),
    path('<int:post_id>/share/',share_post,name='share_post'),


    # path('list/',BlogListView.as_view(),name='list_view')


]