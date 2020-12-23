# Generated by Django 3.1.3 on 2020-12-23 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20201223_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='add',
            options={'managed': True, 'verbose_name': 'Gallery', 'verbose_name_plural': 'Gallery Informations'},
        ),
        migrations.RemoveField(
            model_name='add',
            name='files',
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('add', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.add')),
            ],
            options={
                'verbose_name': 'Gallery Picture',
                'verbose_name_plural': 'Gallery Pictures',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
