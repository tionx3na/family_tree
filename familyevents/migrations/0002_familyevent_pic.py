# Generated by Django 3.1.2 on 2021-01-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familyevent',
            name='pic',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to=''),
        ),
    ]