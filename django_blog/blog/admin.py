from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.

class BlogOwner(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(model_or_iterable=Post, admin_class=BlogOwner)
admin.site.register(Category)
admin.site.register(Tag)
