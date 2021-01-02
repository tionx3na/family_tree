"""family_tree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(r'^jet/', include('jet.urls', 'jet')),              # Django JET URLS
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),                         # Admin Page
    path('', include('landing.urls')),                       # The page for the main landing page
    path('register', include('register.urls')),              # The page for user registration
    path('login', include('login.urls')),                    # The page for user login
    path('home', include('home.urls')),                      # The page for each individual user
    path('myprofile', include('myprofile.urls')),            # The page for each individual user's profile information
    path('familyevents', include('familyevents.urls')),
    path('gallery', include('gallery.urls')),
    path('blog', include('blog.urls')),
    path('tree', include('tree.urls')),
    path('search', include('search.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)