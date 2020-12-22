# Generated by Django 3.1.3 on 2020-12-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=10, null=True)),
                ('day', models.CharField(max_length=10, null=True)),
                ('month', models.CharField(max_length=10, null=True)),
                ('year', models.CharField(max_length=10, null=True)),
                ('content', models.CharField(max_length=100000, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
