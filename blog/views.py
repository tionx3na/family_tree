from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.


@login_required
def Blog(request):
    return render(request, 'blog/blog_page.html')

@login_required
def Post(request):
    return render(request, 'blog/blog_post.html')

@login_required
def Addpost(request):
    form = forms.Blog
    if request.method == 'POST':
        title = request.POST.get('title')
        overview = request.POST.get('overview')
        category = request.FILES.getlist('category')
        content = request.FILES.getlist('content')
        print(title)
        print(overview)
        print(category)
        print(content)
    return render(request, 'blog/blog_addpost.html', {'form': form})