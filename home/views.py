from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AdminPost
from login.models import ActiveInvite
from blog.models import Post
from gallery.models import Add
from familyevents.models import FamilyEvent
from advertisement.models import Advertisement, Adinpage, Thought
from register.forms import NewUser
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(requests):
    if requests.user.username == requests.user.first_name:
        return redirect('newuser')
    if requests.method == 'POST':
        s = requests.POST.get('s')
        return redirect('search', param = s)
    adminpost = AdminPost.objects.all().order_by('-id')[:1]
    users = ActiveInvite.objects.all().order_by('-id')[:4][::-1]
    post = Post.objects.all().order_by('id')[:6][::-1]
    menu = Post.objects.all().order_by('id')[:3][::-1]
    events = FamilyEvent.objects.all().order_by('id')[:8][::-1]
    gallery = Add.objects.all().order_by('id')[:3][::-1]
    ad = Advertisement.objects.all()
    adin = Adinpage.objects.all().order_by('id')[:3][::-1]
    thought = Thought.objects.all().order_by('id')[:1][::-1]
    context = {'adminpost': adminpost, 'users': users, 'post': post, 'events': events, 'gallery': gallery, 'menu': menu, 'ad': ad, 'adin': adin, 'thought': thought}
    return render(requests, 'home/home.html', context)

@login_required
def homepost(requests, title):
    post = AdminPost.objects.filter(title=title)
    context = {'post': post}
    return render(requests, 'home/home_post.html', context)

@login_required
def newuser(requests):
    form2 = NewUser()
    if requests.method == 'POST':
        username = requests.POST.get('username')
        email = requests.POST.get('email')
        password = requests.POST.get('password')

        try:
            user = User.objects.get(username__exact=username)
        except User.DoesNotExist:
            user = None
        if user:
            error = "Username Already exists!"
            context = {'form2': form2, 'error':error}
            return render(requests, 'home/new_user.html', context)

        else:
            user = User.objects.get(username__exact=requests.user)
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()
            activeinvite = ActiveInvite(user=requests.user)
            activeinvite.save()
            return redirect('login')
    context = {'form2': form2}
    return render(requests, 'home/new_user.html', context)

