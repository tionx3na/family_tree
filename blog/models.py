from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField
from login.models import ActiveInvite

User = get_user_model()

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = HTMLField('overview', default=' ')
    content = HTMLField('content', default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.CharField(max_length=50, null=True)
    thumbnail = models.ImageField(blank=False, default='thumbnail.jpg')
    tag = models.CharField(max_length=20, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '1) Post'
        verbose_name_plural = '1) Posts'


    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(ActiveInvite, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = '2) Comment'
        verbose_name_plural = '2) Comments'



    def __str__(self):
        return self.comment

