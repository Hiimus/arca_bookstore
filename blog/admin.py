from django.contrib import admin
from .models import BlogPost, Comment


# Makes the following fields display in admin
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_by',
        'created_at',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
