from django.db import models

# Create your models here.

class FamilyEvent(models.Model):
    author = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=10, null=True)
    day = models.CharField(max_length=10, null=True)
    month = models.CharField(max_length=10, null=True)
    year = models.CharField(max_length=10, null=True)
    content = models.CharField(max_length=100000, null=True)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.first_name
