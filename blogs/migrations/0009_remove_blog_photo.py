# Generated by Django 3.2 on 2022-05-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_blogimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photo',
        ),
    ]
