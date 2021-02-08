from django.urls import path
from . import views

urlpatterns = [
    path('', views.heritage, name="heritage"),  # Pointer to landing page function in views.py
]