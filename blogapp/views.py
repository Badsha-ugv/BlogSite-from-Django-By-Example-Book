from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail 


from django.views.generic import ListView 

from .forms import EmailPostForm
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

# # class view - ListView
# class BlogListView(ListView):
#     queryset = Post.objects.all()
#     context_object_name = 'blogs'
#     paginate_by = 2
#     template_name = 'post_list.html'




def blog_details(request,slug=None):
    if slug != None:
        blog = get_object_or_404(Post,slug=slug)

        return render(request, 'blog_details.html',context={'blog':blog})


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
   
    
