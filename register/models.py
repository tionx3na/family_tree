from django.db import models
from six import python_2_unicode_compatible
import uuid

# Create your models here.


@python_2_unicode_compatible
class PendingInvite(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=100, blank=False)
    comment = models.CharField(max_length=500)
    invite_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_code_active = models.BooleanField(default=True)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Pending Invite'
        verbose_name_plural = 'Pending Invites'

    def __str__(self):
        return self.name

