# Generated by Django 3.1.3 on 2020-12-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeinvite',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
