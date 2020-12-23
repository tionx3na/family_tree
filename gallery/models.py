from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Add(models.Model):
    user = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=60, null=True)
    description = models.CharField(max_length=100000, null=True)
    thumbnail = models.ImageField(blank=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery Informations'

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url

class Pictures(models.Model):
    add = models.ForeignKey(Add, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')



    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Gallery Picture'
        verbose_name_plural = 'Gallery Pictures'

    def __str__(self):
        return self.add

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url