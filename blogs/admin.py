from django.contrib import admin
from .models import Blog, BlogImage

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogImage)
class BlogImageAdmin(admin.ModelAdmin):
    pass