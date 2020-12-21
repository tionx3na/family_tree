from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ActiveInvite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)
    is_code_active = models.BooleanField(default=True)



    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User Information'
        verbose_name_plural = 'User Informations'

    def __str__(self):
        return self.user

