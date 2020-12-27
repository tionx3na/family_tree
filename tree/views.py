from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def tree(requests):
    return render(requests, 'tree/tree_page.html')
