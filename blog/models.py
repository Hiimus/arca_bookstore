from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    image = models.URLField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

