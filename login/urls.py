from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),  # Pointer to register page function in views.py
]