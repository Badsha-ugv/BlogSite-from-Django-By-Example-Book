from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post 


# Create your views here.

def blog_list(request):
    obj = Post.objects.all()
    paginator = Paginator(obj,2)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    

    return render(request, 'post_list.html',context={'blogs':blogs,'page':page}) 

def blog_details(request,slug=None):
    if slug != None:
        blog = get_object_or_404(Post,slug=slug)

        return render(request, 'blog_details.html',context={'blog':blog})
