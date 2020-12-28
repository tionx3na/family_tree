from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

User = get_user_model()

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Categories(models.Model):
    title = models.CharField(max_length=20)




class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField('content', default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.CharField(max_length=50, null=True)
    categories = models.ManyToManyField(Categories)


    def __str__(self):
        return self.title