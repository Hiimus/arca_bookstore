from django import forms
from .models import BlogPost, Comment
from django.forms import TextInput, Textarea


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'created_by']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Write your blog post here...'
                }),
            'image': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Image URL - Optional'
                }),
            'created_by': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Created by:'
                }),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'comment']

        name = forms.CharField(),
        comment = forms.Textarea(),

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Write your comment here...'
                }),
        }
        
        




