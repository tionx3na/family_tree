from django.urls import path
from . import views

urlpatterns = [
    path('<str:param>+param', views.search, name="search"),  # Pointer to landing page function in views.py
]