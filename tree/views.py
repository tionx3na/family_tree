from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from json import dumps
from django.core import serializers


# Create your views here.

@login_required
def tree(requests):
    tree = Tree.objects.all()
    print(tree)
    return render(requests, 'tree/tree_page.html', {'tree': tree})

@login_required
def temp(requests):
    tree = Tree.objects.all()
    print(tree)
    return render(requests, 'tree/temp.html', {'tree': tree})
