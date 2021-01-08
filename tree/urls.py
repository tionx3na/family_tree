from django.urls import path
from . import views

urlpatterns = [
    path('', views.tree, name="tree"),  # Pointer to landing page function in views.py
]