from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),  # Pointer to register page function in views.py
    path('/redirected', views.redirected, name="redirected"),
    path('/more_info', views.more_info, name="more_info"),
]