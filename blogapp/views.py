from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post 


# Create your views here.

def blog_list(request):
    blogs = Post.objects.all()
    return render(request, 'post_list.html',context={'blogs':blogs}) 

def blog_details(request,slug=None):
    if slug != None:
        blog = get_object_or_404(Post,slug=slug)

        return render(request, 'blog_details.html',context={'blog':blog})
