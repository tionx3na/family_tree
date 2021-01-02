from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name="blog"),
    path('post', views.Posts, name="post"),
    path('addpost', views.Addpost, name="addpost"),
    path('blogview/<str:title>+title', views.blogview, name="blogview"),


]
