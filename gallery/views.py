from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Add, Pictures
from blog.models import Post

# Create your views here.

@login_required
def gallery(request):
    gallery = Add.objects.all()
    menu = Post.objects.all().order_by('id')[:3][::-1]
    return render(request, 'gallery/gallery_page.html', {'gallery': gallery, 'menu': menu})

@login_required
def addalbum(request):
    form = forms.Album()
    menu = Post.objects.all().order_by('id')[:3][::-1]
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        thumbnail = request.FILES.getlist('thumbnail')
        files = request.FILES.getlist('files')
        try:
            check = Add.objects.get(title__exact=title)
        except Add.DoesNotExist:
            check = None
        if check:
            error = "The Title Already Exists! Type a unique title."
            return render(request, 'gallery/gallery_add.html', {'form': form, 'menu': menu, 'error': error})
        else:
            user = request.user
            add = Add()
            add.user = user
            add.title = title
            add.description = description
            for t in thumbnail:
                add.thumbnail = t
            add.save()
            for f in files:
                pictures = Pictures()
                pictures.add = Add.objects.get(title=title)
                pictures.image = f
                pictures.save()

            return redirect('gallery')

    return render(request, 'gallery/gallery_add.html', {'form': form, 'menu': menu})

@login_required
def galleryfull(request, title):
    pics = Pictures.objects.filter(add__title=title)
    menu = Post.objects.all().order_by('id')[:3][::-1]
    return render(request, 'gallery/gallery_full.html', {'pics': pics, 'menu': menu})
