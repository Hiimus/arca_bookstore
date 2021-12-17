from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm

# Create your views here.



def view_blog(request):
    """ A view that renders the blog page """

    blogs = BlogPost.objects.all()
    comments = Comment.objects.all()

    form = BlogForm()
    comment_form = CommentForm()

    context = {
        'blogs': blogs,
        'comments': comments,
        'form': form,
        'comment_form': comment_form,
    }

    return render(request, 'blog/view_blogs.html', context)



def add_post(request):
    """ A view that adds post to blog page """

    blogs = BlogPost.objects.all()

    if request.method == "POST":
        form = BlogForm(request.POST)
        
        if form.is_valid:
            form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'Failed to add blog post, please ensure the form is valid')
    else:
        form = BlogForm()

    context = {
        'form': form,
        'blogs': blogs,
    }

    return render(request, 'blog/view_blogs.html', context)


def add_comment(request):
    """ A view that adds comments on the blog page """
    
    comments = Comment.objects.all()
    
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment_form.save()
            messages.success(request, 'Successfully added comment!')
            return redirect(reverse('view_blog'))
        else:
            messages.error(request, 'Failed to add comment, please ensure the form is valid')
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'blog/view_blogs.html', context)