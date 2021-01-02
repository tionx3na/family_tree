# Login models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ActiveInvite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_code_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=20, null=True)
    middle_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    nick_name = models.CharField(max_length=20, null=True)
    mobile1 = models.CharField(max_length=20, null=True)
    mobile2 = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    father = models.CharField(max_length=50,null=True)
    mother = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=500, null=True)
    temp_address = models.CharField(max_length=500, null=True)
    parish = models.CharField(max_length=20, null=True)
    dob = models.CharField(max_length=20, null=True)
    blood = models.CharField(name="blood", max_length=10, null=True)
    occupation = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    occupation_place = models.CharField(max_length=100, null=True)
    spouse_name = models.CharField(max_length=50, null=True)
    spouse_father = models.CharField(max_length=50, null=True)
    spouse_mother = models.CharField(max_length=50, null=True)
    wedding_date = models.CharField(max_length=20, null=True)
    date_edited = models.CharField(max_length=20, null=True)
    #children_number =  models.IntegerField(blank=True, default=0)
    #child1 = models.CharField(max_length=50,blank=True, default=0)
    #child2 = models.CharField(max_length=50,blank=True, default=0)
    #child3 = models.CharField(max_length=50,blank=True, default=0)
    #child4 = models.CharField(max_length=50,blank=True, default=0)
    photo = models.ImageField(blank=True, default='profile_pics/default.jpg')


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User Information'
        verbose_name_plural = 'User Informations'

    def __str__(self):
        return self.user.username

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url


