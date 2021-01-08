from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tree(models.Model):
    Family = models.ForeignKey('self', on_delete=models.CASCADE, related_name='%(class)s_connected_to', null=True, blank=True)
    child_of = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child',null=True, blank=True)
    tag =  models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(blank=True)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Family Tree'
        verbose_name_plural = 'Family Tree Informations'

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class TreeScript(models.Model):
    script = models.TextField(max_length=1000000, null=True, blank=True)
    logo_url = models.CharField(max_length=200, null=True, blank=True)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Family Tree'
        verbose_name_plural = 'Family Tree Informations'



