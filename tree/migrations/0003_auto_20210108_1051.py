# Generated by Django 3.1.2 on 2021-01-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_treescript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treescript',
            name='script',
            field=models.TextField(blank=True, max_length=1000000, null=True),
        ),
    ]