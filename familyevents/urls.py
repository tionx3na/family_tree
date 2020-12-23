from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.events, name="events"),  # Pointer to landing page function in views.py
    path('add_event', views.addevent, name="addevent"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)  # This url pattern allows django to find MEDIA_URL in settings.py