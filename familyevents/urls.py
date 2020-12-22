from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name="events"),  # Pointer to landing page function in views.py
    path('add_event', views.addevent, name="addevent"),
]