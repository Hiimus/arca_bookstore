from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm

# Create your views here.


def view_blogs(request):
    """ A view that renders the blog page """

    blogs = BlogPost.objects.all()
    comments = Comment.objects.all()

    blog_form = BlogForm()

    comment_form = CommentForm()

    context = {
        'blog_form': blog_form,
        'comment_form': comment_form,
        'blogs': blogs,
        'comments': comments,
    }

    return render(request, 'blog/view_blogs.html', context)
