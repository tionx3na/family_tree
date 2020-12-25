from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name="gallery"),  # Pointer to Gallery page function in the views.py
    path('add_album', views.addalbum, name="addalbum"),
    path('gallery_full/<str:title>+title', views.galleryfull, name="galleryfull"),
]
