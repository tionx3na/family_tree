# Generated by Django 3.1.2 on 2021-01-06 09:18

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210106_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=tinymce.models.HTMLField(default=' ', verbose_name='overview'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='thumbnail.jpg', upload_to=''),
        ),
    ]
