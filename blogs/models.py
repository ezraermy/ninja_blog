from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=4000)
    data_published = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, default='default.png')

    def __str__(self):
        return self.blog.title
    
    class Meta:
        verbose_name = 'Blog Image'
        verbose_name_plural = 'Blog Image'