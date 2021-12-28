from django import forms
from .models import BlogPost, Comment
from django.forms import TextInput, Textarea


# Blog form
class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'created_by']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Title'
                }),
            'body': Textarea(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Write your blog post here...'
                }),
            'image': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Image URL - Optional'
                }),
            'created_by': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;',
                'placeholder': 'Created by:'
                }),
        }


# Comment form
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'comment']

        name = forms.CharField(),
        comment = forms.Textarea(),

        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': 'Name'
                }),
            'comment': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;' 'max-height: 200px;',
                'placeholder': 'Write your comment here...'
                }),
        }
        
        




