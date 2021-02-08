from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from json import dumps
from django.core import serializers


# Create your views here.

@login_required
def heritage(requests):

    return render(requests, 'heritage/main_heritage.html')


