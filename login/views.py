from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.models import User, auth
from django .contrib import messages
from .models import *
# Create your views here.
def login(request):
    form = forms.Login()
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username or Password!!')
            return redirect('login')
    else:
        return render(request, 'login/login_page.html', {'form': form})

























