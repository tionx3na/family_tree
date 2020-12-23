from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Add

# Create your views here.

@login_required
def gallery(request):
    gallery = Add.objects.all()
    return render(request, 'gallery/gallery_page.html', {'gallery': gallery})

@login_required
def addalbum(request):
    form = forms.Album()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        thumbnail = request.FILES.getlist('thumbnail')
        files = request.FILES.getlist('files')
        user = request.user
        add = Add()
        add.user = user
        add.title = title
        add.description = description
        for t in thumbnail:
            add.thumbnail = t
        add.save()
        return redirect('gallery')


    return render(request, 'gallery/gallery_add.html', {'form': form})

@login_required
def galleryfull(request):
    return render(request, 'gallery/gallery_full.html',)
