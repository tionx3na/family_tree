from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),  # Pointer to landing page function in views.py
]