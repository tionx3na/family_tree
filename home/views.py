from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminPost
from login.models import ActiveInvite
from blog.models import Post
from gallery.models import Add
from familyevents.models import FamilyEvent

# Create your views here.

@login_required
def home(requests):
    if requests.method == 'POST':
        s = requests.POST.get('s')
        return redirect('search', param = s)
    adminpost = AdminPost.objects.all().order_by('-id')[:1]
    users = ActiveInvite.objects.all().order_by('-id')[:4][::-1]
    post = Post.objects.all().order_by('id')[:6][::-1]
    menu = Post.objects.all().order_by('id')[:3][::-1]
    events = FamilyEvent.objects.all().order_by('id')[:8][::-1]
    gallery = Add.objects.all().order_by('id')[:3][::-1]
    context = {'adminpost': adminpost, 'users': users, 'post': post, 'events': events, 'gallery': gallery, 'menu': menu}
    return render(requests, 'home/home.html', context)

@login_required
def homepost(requests, title):
    post = AdminPost.objects.filter(title=title)
    context = {'post': post}
    return render(requests, 'home/home_post.html', context)

