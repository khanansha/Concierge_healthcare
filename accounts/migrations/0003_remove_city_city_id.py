# Generated by Django 2.0.2 on 2020-05-05 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='city_id',
        ),
    ]
