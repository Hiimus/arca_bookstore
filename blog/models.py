from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=1000)
    image = models.URLField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'BlogPost', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='comments')

    def __str__(self):
        return self.name
