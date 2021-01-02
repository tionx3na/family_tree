from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post,Author, Comments
from login.models import ActiveInvite


# Create your views here.


@login_required
def Blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog/blog_page.html', {'blogs': blogs})

@login_required
def Posts(request):
    return render(request, 'blog/blog_post.html')

@login_required
def Addpost(request):
    form = forms.Blog
    if request.method == 'POST':
        title = request.POST.get('title')
        thumbnail = request.FILES.getlist('thumbnail')
        overview = request.POST.get('overview')
        tag = request.POST.get('tag')
        content = request.POST.get('content')
        author = request.user
        comment_count = 0
        post1 = Post()
        post1.title = title
        post1.overview = overview
        for t in thumbnail:
            post1.thumbnail = t
        post1.content = content
        post1.author = author
        post1.comment_count = comment_count
        post1.tag = tag
        post1.save()
        return redirect('blog')

    return render(request, 'blog/blog_addpost.html', {'form': form})

@login_required
def blogview(request, title):
    post = Post.objects.filter(title=title)
    cmnt = Comments.objects.filter(post__title=title)
    activeinvite = ActiveInvite.objects.filter(user=request.user)
    if request.method == 'POST':
        user = request.user
        comment = request.POST.get('comment')
        l = Post.objects.get(title=title)
        c = Comments()
        c.user = user
        c.post = l
        c.comment = comment
        c.save()

    return render(request,'blog/blog_post.html', {'post': post, 'comments': cmnt, 'ai': activeinvite})