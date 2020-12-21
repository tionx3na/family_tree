from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(requests):
    return render(requests, 'home/home_page.html')
