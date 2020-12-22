from django.urls import path
from . import views

urlpatterns = [
    path('', views.myprofile, name="myprofile"),  # Pointer to register page function in views.py
    path('logout', views.userlogout, name="logout"),
]