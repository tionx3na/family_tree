from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from json import dumps
from django.core import serializers


# Create your views here.

@login_required
def tree(requests):
    tree = TreeScript.objects.all()
    return render(requests, 'tree/tree_page.html', {'tree': tree})

@login_required
def h_tree(requests):
    tree = TreeScript.objects.all()
    return render(requests, 'tree/h_tree.html', {'tree': tree})


