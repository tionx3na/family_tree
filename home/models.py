from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

# Create your models here.

class AdminPost(models.Model):
    title = models.CharField(max_length=100)
    overview = HTMLField('overview', default=0)
    content = HTMLField('content', default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null=True)
    thumbnail = models.ImageField(blank=False, default=0)
    tag = models.CharField(max_length=20, null=True)




    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Post by Admin'
        verbose_name_plural = 'Posts by Admin'

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url




