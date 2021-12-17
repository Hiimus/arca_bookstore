from django import forms
from .models import BlogPost, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'body', 'image', 'created_by',)

        title = forms.CharField(),
        body = forms.Textarea(),
        image = forms.URLField(),
        created_by = forms.CharField(),


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'comment')

        name = forms.CharField(),
        comment = forms.Textarea(),
        
        
