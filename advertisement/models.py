from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=150, null=True)
    photo = models.ImageField(blank=True, default='profile_pics/default.jpg')


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Main Page Ad'
        verbose_name_plural = 'Main Page ads'

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


# Create your models here.
class Adinpage(models.Model):
    title = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=150, null=True)
    photo = models.ImageField(blank=True, default='profile_pics/default.jpg')


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'In Page Ad'
        verbose_name_plural = 'In Page Ads'

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

class Thought(models.Model):
    thought = models.CharField(max_length=500, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Thought of the Day'
        verbose_name_plural = 'Thought of the Day'

    def __str__(self):
        return self.thought

