# Generated by Django 3.1.3 on 2020-12-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201228_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail',
            new_name='image',
        ),
    ]
