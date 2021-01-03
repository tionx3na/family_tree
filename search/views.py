from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from login.models import ActiveInvite
from blog.models import Post

# Create your views here.

@login_required
def search(requests, param):
    arg = param
    first_name = ''
    middle_name = ''
    last_name = ''
    blog = ' '
    if requests.method == 'POST':
        s = requests.POST.get('search')
        arg = s
        arg = arg.split()
        for i in arg:
            arg = i.capitalize()
            print(arg)
            first_name = ActiveInvite.objects.filter(first_name__icontains=arg)
            middle_name = ActiveInvite.objects.filter(middle_name=arg)
            last_name = ActiveInvite.objects.filter(last_name=arg)
    print(first_name)
    print(middle_name)
    print(last_name)
    print(blog)
    context = {'first_name': first_name, 'middle_name': middle_name, 'last_name': last_name, 'blog': blog, 'arg': arg}
    return render(requests, 'search/search_page.html', context)
