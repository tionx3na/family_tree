# Generated by Django 3.1.3 on 2020-12-28 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201228_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='thumbnail',
        ),
    ]
