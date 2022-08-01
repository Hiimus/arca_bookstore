from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm


# Create your views here.


def view_blog(request):
    """ A view that renders the blog page """

    blogs = BlogPost.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')

    form = BlogForm()
    comment_form = CommentForm()

    context = {
        'blogs': blogs,
        'comments': comments,
        'form': form,
        'comment_form': comment_form,
    }

    return render(request, 'blog/view_blogs.html', context)


def blog_info(request, blog_id):
    """ A view that renders the blog info page """

    blog = get_object_or_404(BlogPost, pk=blog_id)
    comments = blog.comments.all().order_by('-created_at')

    form = BlogForm()
    comment_form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_info.html', context)


@login_required
def add_post(request):
    """ A view that adds post to blog page """

    blogs = BlogPost.objects.all()

    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid:
            form.save()
            messages.info(request, 'Successfully added blog post!')
            return redirect(reverse('view_blog'))
        else:
            messages.error(
                request, 'Failed to add blog post, \
                    please ensure the form is valid')
    else:
        form = BlogForm()

    context = {
        'form': form,
        'blogs': blogs,
    }

    return render(request, 'blog/view_blogs.html', context)


@login_required
def delete_post(request, blog_id):
    """ Delete a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('view_blog'))

    if request.method == 'POST':
        blog = get_object_or_404(BlogPost, pk=blog_id)
        print(blog)
        blog.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('view_blog'))
    return render(request, 'delete_blog.html')


@login_required
def edit_post(request, blog_id):
    """ Edit a post from the blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('view_blog'))

    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully updated blog post!')
            return redirect(reverse('view_blog'))
        else:
            messages.error(
                request, 'Failed to update post.\
                    Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def add_comment(request, blog_id):
    """ A view that adds comments on the blog page """

    blog = get_object_or_404(BlogPost, pk=blog_id)
    comments = blog.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.post = blog
            comment.save()
            messages.info(request, 'Successfully added comment!')
            return redirect(reverse('blog_info', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add comment,\
                please ensure the form is valid')
    else:
        comment_form = CommentForm()

    context = {
        'comments': comments,
        'comment_form': comment_form,
        'blog': blog,
    }

    return render(request, 'blog/blog_info.html', context)


@login_required
def delete_comment(request, comment_id):
    """ A view that deletes blog post comment"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    comment = Comment.objects.all().filter(pk=comment_id)
    comment.delete()

    messages.info(request, 'Comment deleted!')
    return redirect(reverse('view_blog'))
