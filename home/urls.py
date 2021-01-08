from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # Pointer to landing page function in views.py
    path('home/<str:title>+title', views.homepost, name="homepost"),
    path('newuser', views.newuser, name="newuser"),
]