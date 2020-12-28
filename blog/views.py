from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Post,Categories,Author


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
        overview = request.POST.get('overview')
        category = request.FILES.getlist('category')
        content = request.FILES.getlist('content')
        
        author = request.user
        comment_count = 0
        post1 = Post()
        post1.title = title
        post1.overview = overview
        
        post1.content = content
        post1.author = author
        post1.comment_count = comment_count
        for cat in category:
            post1.categories.add(cat)
        post1.save()
        print(post1)
        return redirect('blog')

    return render(request, 'blog/blog_addpost.html', {'form': form})

@login_required
def blogview(request):
    return render(request,'blog/blog_post.html')