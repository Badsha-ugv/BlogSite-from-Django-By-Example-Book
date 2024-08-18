from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail 
from taggit.models import Tag



# import from models 
from .forms import EmailPostForm, CommentForm
from .models import Post, Comment


# Create your views here.

def blog_list(request,tag_slug=None):
    obj = Post.objects.all()
    tag = None 

    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        obj = obj.filter(tags__in=[tag])

    paginator = Paginator(obj,2)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    

    return render(request, 'post_list.html',context={'blogs':blogs,'page':page,'tag':tag}) 


def blog_details(request,slug=None):
    
    blog = get_object_or_404(Post,slug=slug)
    comment = blog.comments.filter(active=True)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = blog 
            new_comment.save()
       
    elif request.method == 'GET':
        form = CommentForm()
        context = {
            'blog':blog,
            'form':form,
            'comments':comment
        }
        return render(request, 'blog_details.html',context)


def share_post(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    if post:
        print(post)
    else:
        print('Post not found')
    sent = False 

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f'{cd['name']} ({cd['email']}) recommends you reading "{post.title}"'

            message = f'Read "{post.title}" at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}'

            send_mail(subject, message, 'badsha.ugv@myblog.com',  [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post':post,
        'form':form
    }
    return render(request,'share_post.html',context)
   
    
