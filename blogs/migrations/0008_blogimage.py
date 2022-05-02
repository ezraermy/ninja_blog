# Generated by Django 3.2 on 2022-05-02 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20220430_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blog')),
            ],
            options={
                'verbose_name': 'Blog Image',
                'verbose_name_plural': 'Blog Image',
            },
        ),
    ]