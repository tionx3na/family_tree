from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from login.models import ActiveInvite
from blog.models import Post

# Create your views here.

@login_required
def search(requests, param):
    if param == ' ':
        param = None
    if requests.method == 'POST':
        param = requests.POST.get('search')
        print(param)
    username = ActiveInvite.objects.filter(user=param)
    first_name = ActiveInvite.objects.filter(first_name=param)
    middle_name = ActiveInvite.objects.filter(middle_name=param)
    last_name = ActiveInvite.objects.filter(last_name=param)
    blog = Post.objects.filter(title=param)
    context = {'username': username, 'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'blog': blog, 'param': param}
    return render(requests, 'search/search_page.html', context)
