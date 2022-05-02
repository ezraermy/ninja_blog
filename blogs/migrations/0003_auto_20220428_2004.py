# Generated by Django 3.2 on 2022-04-28 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='thumb',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blog')),
            ],
        ),
    ]
