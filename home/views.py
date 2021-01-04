from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(requests):
    if requests.method == 'POST':
        s = requests.POST.get('s')
        return redirect('search', param = s)
    return render(requests, 'home/home_page.html')
