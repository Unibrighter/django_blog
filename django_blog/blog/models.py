from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.utils.html import strip_tags
import markdown

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    view_count = models.PositiveIntegerField(default = 0)

    excerpt = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs = {'post_id': self.pk})

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def save(self, *args, **kwargs):   
        if (not self.excerpt):
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time','title']

